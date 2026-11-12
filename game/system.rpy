# ==============================================================================
# 1. CALLBACK SISTEM BICARA & ANIMASI SPRITE
# ==============================================================================
init -1 python:
    def speaker_callback(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "begin":
            speaking_char = renpy.get_say_image_tag()
            for tag in renpy.get_showing_tags(layer='master'):
                if tag.startswith("bg") or tag.startswith("cg") or tag.startswith("cutin"):
                    continue
                if tag == speaking_char:
                    renpy.show(tag, at_list=[talk_active])
                else:
                    renpy.show(tag, at_list=[talk_dim])

        # --- FITUR SUARA BLIP DIALOG (Aktifkan jika ada audio/blip.ogg) ---
        # elif event == "show_done":
        #     renpy.sound.play("audio/blip.ogg", loop=True)
        # elif event == "slow_done" or event == "end":
        #     renpy.sound.stop()

# ==============================================================================
# 2. TRANSFORM & ANIMASI ATL
# ==============================================================================
transform center_breathe:
    xalign 0.5 yalign 1.0
    subpixel True
    block:
        ease 1.8 yoffset -6
        ease 1.8 yoffset 0
        repeat

transform monster_pos:
    xalign 0.5 yalign 0.45
    subpixel True
    block:
        ease 1.2 yoffset -10
        ease 1.2 yoffset 0
        repeat

transform talk_active:
    subpixel True
    parallel:
        easein 0.15 matrixcolor BrightnessMatrix(0.0) alpha 1.0 zoom 1.03
    parallel:
        easein 0.1 yoffset -18
        easeout 0.1 yoffset 0
        block:
            ease 1.8 yoffset -6
            ease 1.8 yoffset 0
            repeat

transform talk_dim:
    subpixel True
    easeout 0.15 matrixcolor BrightnessMatrix(-0.35) alpha 0.85 zoom 0.96
    yoffset 0

transform hit_flash:
    parallel:
        matrixcolor TintMatrix("#ff0000")
        linear 0.06 xoffset -20
        linear 0.06 xoffset 20
        linear 0.06 xoffset -10
        linear 0.06 xoffset 10
        linear 0.06 xoffset 0 matrixcolor TintMatrix("#ffffff")

transform enemy_lunge:
    easein 0.12 zoom 1.25 yoffset 30
    easeout 0.15 zoom 1.0 yoffset 0

transform skill_cutin_anim:
    xalign -1.0 yalign 0.35 alpha 0.0
    easein 0.15 xalign 0.5 alpha 1.0
    linear 0.5 xalign 0.5
    easeout 0.15 xalign 2.0 alpha 0.0

transform cg_dramatic_zoom:
    subpixel True
    zoom 1.0 xalign 0.5 yalign 0.5
    easein 15.0 zoom 1.12

transform float_up:
    xalign 0.5 yalign 0.35 alpha 1.0
    easeout 1.1 yoffset -70 alpha 0.0

# ==============================================================================
# 3. CUSTOM SCREEN / UI
# ==============================================================================
screen popup_stat(teks, warna="#ffdd55"):
    zorder 100
    text "[teks]" size 42 color warna outlines [(3, "#000000", 0, 0)] at float_up
    timer 1.1 action Hide("popup_stat")

screen status_hud():
    frame:
        xalign 0.01 yalign 0.01
        padding (15, 12)
        background Solid("#000000cc")
        vbox:
            spacing 3
            $ w_atk = WEAPON_DB[senjata]["atk"]
            $ w_def = WEAPON_DB[senjata]["def"]
            $ aff_atk = (ellen_affection // 10) * 5
            $ total_atk_hud = w_atk + aff_atk
            $ cleared_count = len(gates_cleared)
            $ endings_count = len(endings_unlocked)

            text "Kesatria [player_name] | Siklus ke-[loop_count]" size 18 color "#ffffff"
            text "HP: [hp] / [max_hp]" size 17 color "#2ed573"
            text "Gold: [gold] | Shards: [remnant_shards]" size 17 color "#ffd32a"
            text "Senjata: [senjata]" size 16 color "#70a1ff"
            text "ATK Total: [total_atk_hud] | DEF: [w_def]" size 15 color "#ffa502"
            null height 4
            text "ellen Affection: [ellen_affection] | Eksistensi: [ellen_existence] Poin" size 16 color "#ff6b81"
            text "Gerbang Selesai: [cleared_count]/10 | Takdir: [endings_count]/26" size 15 color "#a4b0be"

# ==============================================================================
# 4. DATABASE & VARIABEL STATUS
# ==============================================================================
init python:
    WEAPON_DB = {
        "Pedang Karatan": {"atk": 15, "def": 0, "desc": "Pedang tua yang nyaris patah."},
        "Tongkat Sihir Yggdrasil": {"atk": 45, "def": 10, "desc": "Peninggalan peri hutan gelap."},
        "Pedang Excalibur": {"atk": 65, "def": 15, "desc": "Pedang suci dari puncak Bukit Angin."},
        "Aegis Shield": {"atk": 30, "def": 45, "desc": "Perisai magis dengan pertahanan mutlak."},
        "Tombak Abyssal": {"atk": 85, "def": 25, "desc": "Senjata kuno dari dasar samudra."}
    }

default player_name = "Kesatria"
default hp = 100
default max_hp = 100
default gold = 50
default senjata = "Pedang Karatan"
default inventory_weapons = ["Pedang Karatan"]

default loop_count = 1
default ellen_affection = 0
default ellen_existence = 100
default remnant_shards = 0
default gates_cleared = set()
default endings_unlocked = set()
default world_peace_chess = False

# ==============================================================================
# 5. MESIN PERTARUNGAN (ROGUE-LITE COMBAT)
# ==============================================================================
label start_combat(enemy_name, enemy_hp_val, enemy_atk_val, reward_gold, reward_shard=1):
    $ c_enemy_name = enemy_name
    $ c_enemy_hp = enemy_hp_val
    $ c_enemy_atk = enemy_atk_val
    $ c_reward_gold = reward_gold
    $ c_reward_shard = reward_shard

    hide npc
    show enemy at monster_pos with dissolve
    sys "PERTARUNGAN DIMULAI: Melawan [c_enemy_name] (HP: [c_enemy_hp] | ATK: [c_enemy_atk])!"

    label combat_turn:
        $ total_atk = WEAPON_DB[senjata]["atk"] + ((ellen_affection // 10) * 5)
        $ burst_atk = total_atk * 2
        $ total_def = WEAPON_DB[senjata]["def"]

        menu:
            "[c_enemy_name] (HP: [c_enemy_hp]) bersiap menyerang!"

            "Tebas dengan [senjata] (Damage: [total_atk])":
                $ c_enemy_hp -= total_atk
                show enemy at hit_flash
                show screen popup_stat("-[total_atk] HP!", "#ff4757")
                with vpunch
                "Kamu menyerang [c_enemy_name] dan memberikan [total_atk] damage!"

            "Serangan Ikatan Jiwa (Damage: [burst_atk], Butuh 15 HP)" if hp > 15 and ellen_affection >= 20:
                $ hp -= 15
                $ c_enemy_hp -= burst_atk
                show cutin_ellen at skill_cutin_anim
                show enemy at hit_flash
                show screen popup_stat("CRITICAL! -[burst_atk] HP!", "#ffdd55")
                with vpunch
                "Cahaya ingatan ellen menyelimuti senjatamu! Kamu menebas sebesar [burst_atk] damage!"
                hide cutin_ellen

            "Kabur ke Sanctuary (-10 Eksistensi ellen)":
                $ ellen_existence -= 10
                hide enemy with dissolve
                show screen popup_stat("Eksistensi ellen -10", "#ff4757")
                "Kamu mundur paksa menembus kabut dimensi!"
                jump sanctuary_hub

        if c_enemy_hp <= 0:
            hide enemy with zoomout
            $ gold += c_reward_gold
            $ remnant_shards += c_reward_shard
            show screen popup_stat("+[c_reward_gold] Gold | +[c_reward_shard] Shard!", "#ffd32a")
            sys "KEMENANGAN! Kamu mendapat [c_reward_gold] Gold dan [c_reward_shard] Pecahan Memori!"
            return

        $ dmg_taken = max(5, c_enemy_atk - total_def)
        $ hp -= dmg_taken
        show enemy at enemy_lunge
        show screen popup_stat("Terkena -[dmg_taken] HP!", "#ff4757")
        with hpunch
        "[c_enemy_name] menghantammu! (Terkena [dmg_taken] damage setelah dikurangi [total_def] DEF)."
        show enemy at monster_pos

        if hp <= 0:
            hide enemy
            jump player_death_cycle

        jump combat_turn