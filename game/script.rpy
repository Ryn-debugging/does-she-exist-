# ==============================================================================
# 1. DEFINISI KARAKTER
# ==============================================================================
define p = Character("[player_name]", color="#dcdde1", image="player", callback=speaker_callback)
define e = Character("Ellen", color="#ff6b81", what_prefix='"', what_suffix='"', image="ellen", callback=speaker_callback)
define sys = Character("Takdir", color="#eccc68", what_prefix='(( ', what_suffix=' ))', callback=speaker_callback)
define npc = Character("Entitas", color="#a4b0be", what_prefix='"', what_suffix='"', image="npc", callback=speaker_callback)

# ==============================================================================
# 2. GAMBAR BACKGROUND & PLACEHOLDER SPRITE
# ==============================================================================
image bg black = Solid("#000000")
image bg sanctuary = Solid("#130f40")
image bg forest = Solid("#0b2919")
image bg lava = Solid("#3d0c02")
image bg wind = Solid("#1e272e")
image bg desert = Solid("#4a3512")
image bg ice = Solid("#0a3d62")
image bg pirate = Solid("#192a56")
image bg castle = Solid("#2f3640")
image bg swamp = Solid("#211a30")
image bg sky = Solid("#273c75")
image bg ocean = Solid("#051426")

image ellen = Composite(
    (320, 620),
    (0, 0), "images/karakter/ellen.png",
)

image npc = Composite(
    (320, 580),
    (0, 0), Solid("#7bed9f"),
    (20, 20), Text("SPRITE ENTITAS / NPC\n(Auto-Dimming)", size=22, color="#000000", text_align=0.5)
)

image enemy = Composite(
    (380, 420),
    (0, 0), Solid("#ff4757"),
    (20, 20), Text("SPRITE MONSTER\n(Hit Flash & Shake)", size=24, color="#ffffff", text_align=0.5)
)

image cutin_ellen = Composite(
    (1280, 220),
    (0, 0), Solid("#ff6b81dd"),
    (400, 75), Text(">> SERANGAN IKATAN JIWA! <<", size=45, color="#ffffff", outlines=[(3, "#000000", 0, 0)])
)

# ==============================================================================
# 3. MULAI PERMAINAN
# ==============================================================================
label start:
    scene bg black with fade
    "Dunia telah hancur menjadi sepuluh kepingan dongeng yang membusuk."
    "Kamu terbangun di ambang kehampaan, memegang sebilah pedang yang nyaris hancur."

    $ input_nama = renpy.input("Masukkan nama kesatria kamu:", default="Arthur", length=15)
    $ input_nama = input_nama.strip()
    if input_nama != "":
        $ player_name = input_nama

    show screen status_hud
    scene bg sanctuary at cg_dramatic_zoom with dissolve
    show ellen at center_breathe with dissolve

    e "Kau akhirnya bangun, [player_name]..."
    p "kamu? Tempat apa ini...?"
    e "aku adalah ellen... mungkin kamu tidak mengingatku, tapi aku adalah satu-satunya yang tersisa dari dunia ini."
    e "semua orang sudah mati di luar sana, dan aku hanya bisa menunggu di sini..."
    e "ada cara untuk menyelamatkan dunia ini, tapi itu akan sangat berbahaya. Aku tidak bisa melakukannya sendiri."
    e "aku membutuhkanmu untuk menembus gerbang-gerbang itu dan mengumpulkan kepingan jiwaku yang hilang."
    e "Jika kau mati di luar sana, kau akan kembali ke ruangan ini... namun kosekuensi nya sebagian dari diriku dan ingatanku tentangmu akan terhapus sebagai bayarannya."
    e "Kumohon, kembalilah dengan selamat ksatria ku aku akan menunggu mu disini... selalu."

    jump sanctuary_hub

# ==============================================================================
# 4. SIKLUS KEMATIAN & ENDING
# ==============================================================================
label player_death_cycle:
    scene bg black with fade
    "Penglihatan mu menjadi gelap gulita.... Nyawamu terenggut oleh Gerbang Takdir..."
    "Namun benang jiwamu di tarik ellen.... menarikmu kembali ke Sanctuary dengan harga yang menyakitkan."

    $ loop_count += 1
    $ hp = max_hp
    $ ellen_existence -= 25
    show screen popup_stat("Eksistensi Ellen -25!", "#ff4757")

    sys "SIKLUS BERULANG (Loop ke-[loop_count]). Eksistensi Ellen terkuras untuk menghidupkanmu kembali!"
    jump sanctuary_hub

label bad_ending_nonexistent:
    hide screen status_hud
    $ total_endings = len(endings_unlocked)
    scene bg black with fade
    "Ketika kesadaranmu pulih di Sanctuary, ruangan itu terasa sangat dingin dan sunyi."
    "Tidak ada siapa-siapa di sana."
    "Kamu melihat cangkir teh di atas meja, namun kamu tidak bisa mengingat siapa yang pernah duduk di hadapanmu."
    "Nama gadis itu, suaranya, dan senyumnya telah terhapus sepenuhnya dari ingatanmu karena kamu gagal dalam misi mu....."
    "BAD ENDING: antara kamu dan keberadaan ku\n(Total Siklus: [loop_count] | Takdir Terbuka: [total_endings]/26)"
    return

label true_ending_route:
    scene bg sanctuary at cg_dramatic_zoom with dissolve
    show ellen at center_breathe with dissolve
    $ total_endings = len(endings_unlocked)
    e "[player_name]... Kau telah menaklukkan begitu banyak gerbang takdir dan mengumpulkan kepingan jiwaku."
    e "Berkat ikatan kita, tubuhku tidak lagi memudar. Aku benar-benar nyata sekarang."
    
    if len(gates_cleared) == 10:
        e "Bahkan seluruh 10 Gerbang Mimpi Buruk telah kau tundukkan sepenuhnya!"
    
    p "Ayo kita tinggalkan tempat hampa ini, ellen. Kita bangun dunia baru di luar sana."
    e "Ya! Ke mana pun kau melangkah, aku akan selalu berada di sisimu."

    hide screen status_hud
    scene bg sky at cg_dramatic_zoom with fade
    "Cahaya hangat meruntuhkan dinding Sanctuary. Kalian berdua melangkah keluar menuju fajar yang baru."
    "TRUE ENDING: MELAMPAUI SEPULUH GERBANG TAKDIR\n(Selamat! Kesatria [player_name] menamatkan game dalam [loop_count] Siklus dengan [total_endings]/26 Takdir Terbuka!)"
    return