label sanctuary_hub:
    scene bg sanctuary at cg_dramatic_zoom with dissolve
    show ellen at center_breathe

    if ellen_existence <= 0:
        jump bad_ending_nonexistent

    menu:
        "Apa yang ingin kamu lakukan di Sanctuary?"

        "Pilih Gerbang Wilayah (1-10 Gerbang Takdir)":
            jump gate_selection

        "Habiskan Waktu Bersama ellen (Menu Dating & Pemulihan)":
            jump dating_menu

        "Persenjataan & Upgrade Diri (Gunakan Gold)":
            jump shop_menu

        "Buka Gerbang Kebenaran (TAMATKAN GAME)" if len(gates_cleared) >= 5 and ellen_affection >= 80:
            jump true_ending_route

# --- MENU DATING SIM ---
label dating_menu:
    show ellen at center_breathe
    menu:
        e "Ada apa, [player_name]? Kau ingin duduk di dekatku?"

        "Ngobrol dari hati ke hati (+10 Affection, Butuh 20 Gold untuk teh hangat)" if gold >= 20:
            $ gold -= 20
            $ ellen_affection += 10
            show screen popup_stat("Affection +10!", "#ff6b81")
            if ellen_affection <= 30:
                e "Terima kasih tehnya... Sudah lama sekali sejak terakhir kali ada seseorang yang menganggapku benar-benar ada di dunia ini."
            elif ellen_affection <= 70:
                e "Setiap kali kau pergi menembus gerbang itu, dadaku terasa sesak. Jangan mati konyol di luar sana, mengerti?"
            else:
                e "Meskipun dunia ini hanyalah dongeng yang busuk, selama kau menggenggam tanganku, aku merasa nyata."
            sys "Affection ellen naik +10! Kekuatan seranganmu di gerbang bertambah."
            jump dating_menu

        "Berikan Hadiah Cincin Emas (+25 Affection, Butuh 150 Gold)" if gold >= 150:
            $ gold -= 150
            $ ellen_affection += 25
            show screen popup_stat("Affection +25!", "#ff6b81")
            e "I-ini untukku? Bodoh... untuk apa memberikan barang mewah di dunia yang sudah hancur? Tapi... akan kujaga baik-baik."
            sys "Affection ellen melonjak +25!"
            jump dating_menu

        "Gunakan Pecahan Memori untuk memulihkan eksistensinya (+30 Eksistensi, Butuh 1 Shard)" if remnant_shards >= 1:
            $ remnant_shards -= 1
            $ ellen_existence = min(100, ellen_existence + 30)
            $ ellen_affection += 10
            show screen popup_stat("Eksistensi +30! Affection +10!", "#70a1ff")
            e "Ah... bayangan tubuhku kembali utuh. Aku ingat sekarang, namaku, suaramu, dan janji kita."
            sys "Eksistensi ellen pulih 30 poin!"
            jump dating_menu

        "Minta ellen mengobati lukamu (Pulihkan HP Penuh, Gratis jika Affection >= 30)" if hp < max_hp:
            if ellen_affection >= 30:
                $ hp = max_hp
                show screen popup_stat("HP Pulih Penuh!", "#2ed573")
                e "Kemarikan tanganmu. Biarkan sihirku menutup luka-lukamu."
                sys "HP pulih sepenuhnya berkat kasih sayang ellen!"
            else:
                e "Maaf... ikatan jiwa kita belum cukup kuat untuk menyalurkan sihir penyembuh secara cuma-cuma."
                sys "Butuh minimal 30 Affection agar ellen bisa menyembuhkanmu gratis!"
            jump dating_menu

        "Kembali ke Menu Utama":
            jump sanctuary_hub

# --- MENU TOKO & SENJATA ---
label shop_menu:
    $ weapon_count = len(inventory_weapons)
    menu:
        "Tempat Tempa & Peralatan Sanctuary:"

        "Istirahat & Perban Luka (Pulihkan HP Penuh - 30 Gold)" if hp < max_hp and gold >= 30:
            $ gold -= 30
            $ hp = max_hp
            show screen popup_stat("HP Penuh! (-30 Gold)", "#2ed573")
            sys "Kamu beristirahat dan membalut luka. HP kembali penuh!"
            jump shop_menu

        "Tingkatkan Kapasitas Fisik (+25 Max HP Permanen - 100 Gold)" if gold >= 100:
            $ gold -= 100
            $ max_hp += 25
            $ hp += 25
            show screen popup_stat("Max HP +25!", "#2ed573")
            sys "Batas Maksimal HP meningkat menjadi [max_hp]!"
            jump shop_menu

        "Beli Pecahan Memori di Altar (200 Gold -> 1 Shard)" if gold >= 200:
            $ gold -= 200
            $ remnant_shards += 1
            show screen popup_stat("+1 Memory Shard!", "#70a1ff")
            sys "Kamu menukar 200 Gold menjadi 1 Pecahan Memori."
            jump shop_menu

        "Ganti Senjata yang Digunakan ([weapon_count] dimiliki)":
            jump equip_weapon_menu

        "Kembali":
            jump sanctuary_hub

label equip_weapon_menu:
    python:
        choices = []
        for w in inventory_weapons:
            stats = WEAPON_DB[w]
            label_text = "{} (ATK: {} | DEF: {})".format(w, stats['atk'], stats['def'])
            choices.append((label_text, w))
        choices.append(("Kembali", "back"))
        selected = renpy.display_menu(choices)

    if selected != "back":
        $ senjata = selected
        show screen popup_stat("Equipped: [senjata]", "#ffa502")
        sys "Kamu sekarang menggunakan [senjata]!"
    jump shop_menu