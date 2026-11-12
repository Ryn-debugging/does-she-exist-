label gate_selection:
    scene bg black with dissolve
    $ g1 = "[Selesai]" if 1 in gates_cleared else ""
    $ g2 = "[Selesai]" if 2 in gates_cleared else ""
    $ g3 = "[Selesai]" if 3 in gates_cleared else ""
    $ g4 = "[Selesai]" if 4 in gates_cleared else ""
    $ g5 = "[Selesai]" if 5 in gates_cleared else ""
    $ g6 = "[Selesai]" if 6 in gates_cleared else ""

    menu:
        "Pilih Gerbang dunia yang ingin kamu tuju (1-6):"
        "1. Hutan Gelap [g1]":
            jump gate_1_forest
        "2. Lembah Lahar [g2]":
            jump gate_2_lava
        "3. Bukit Angin [g3]":
            jump gate_3_wind
        "4. Gurun Pasir [g4]":
            jump gate_4_desert
        "5. Gunung Es [g5]":
            jump gate_5_ice
        "6. Teluk Bajak Laut [g6]":
            jump gate_6_pirate
        "Lihat Gerbang 7 sampai 10":
            jump gate_selection_page2
        "Batal & Kembali ke Sanctuary":
            jump sanctuary_hub

label gate_selection_page2:
    $ g7 = "[Selesai]" if 7 in gates_cleared else ""
    $ g8 = "[Selesai]" if 8 in gates_cleared else ""
    $ g9 = "[Selesai]" if 9 in gates_cleared else ""
    $ g10 = "[Selesai]" if 10 in gates_cleared else ""

    menu:
        "Pilih Gerbang Wilayah yang ingin kamu tuju (7-10):"
        "7. Kastil Tua [g7]":
            jump gate_7_castle
        "8. Rawa Misteri [g8]":
            jump gate_8_swamp
        "9. Kota Langit [g9]":
            jump gate_9_sky
        "10. Dasar Samudra [g10]":
            jump gate_10_ocean
        "Kembali ke Gerbang 1-6":
            jump gate_selection

# --- WILAYAH 1: HUTAN GELAP ---
label gate_1_forest:
    scene bg forest at cg_dramatic_zoom with dissolve
    "Kamu memasuki Hutan Gelap yang berkabut tebal. Bau lumut dan bangkai menyengat hidungmu."
    "Di tengah jalan, kamu menemukan jalan setapak yang terbelah dua."

    menu:
        "Ikuti jalan setapak bercahaya":
            show npc at center_breathe with dissolve
            "Kamu tiba di danau suci yang airnya berkilau pucat dan melihat sesosok peri pelindung hutan."
            menu:
                "Sapa peri dengan ramah":
                    $ gold += 50
                    $ endings_unlocked.add("Ending 5: Berkah Peri Hutan")
                    $ gates_cleared.add(1)
                    show screen popup_stat("+50 Gold!", "#ffd32a")
                    npc "Manusia yang sopan jarang ditemukan di dunia yang sekarat ini. Ambillah koin ini dan pulanglah."
                    sys "(TAKDIR 5 TERBUKA): Peri memberimu 50 Gold lalu mengantarmu kembali ke Sanctuary."
                    jump sanctuary_hub

                "Ikuti peri diam-diam dari belakang":
                    hide npc with dissolve
                    "Peri itu terbang masuk ke dalam celah Pohon Raksasa bercahaya."
                    menu:
                        "Ketuk pintu pohon dan minta izin masuk":
                            show npc at center_breathe with dissolve
                            "Peri itu terkejut, namun mengagumi adabmu! Di dalam pohon ada dua peti kuno."
                            menu:
                                "Buka Peti Emas":
                                    $ gold += 500
                                    $ endings_unlocked.add("Ending 1: Harta Pohon Raksasa")
                                    $ gates_cleared.add(1)
                                    show screen popup_stat("+500 Gold!", "#ffd32a")
                                    sys "(TAKDIR 1 TERBUKA): Peti berisi harta melimpah! Kamu mendapat +500 Gold!"
                                    jump sanctuary_hub

                                "Buka Peti Kayu Tua":
                                    if "Tongkat Sihir Yggdrasil" not in inventory_weapons:
                                        $ inventory_weapons.append("Tongkat Sihir Yggdrasil")
                                    $ senjata = "Tongkat Sihir Yggdrasil"
                                    $ endings_unlocked.add("Ending 2: Warisan Yggdrasil")
                                    $ gates_cleared.add(1)
                                    show screen popup_stat("Senjata Baru: Tongkat Yggdrasil!", "#70a1ff")
                                    sys "(TAKDIR 2 TERBUKA): Kamu mendapatkan senjata legendaris 'Tongkat Sihir Yggdrasil' (ATK 45)!"
                                    jump sanctuary_hub

                        "Cari celah jendela untuk mengintip":
                            show npc at center_breathe with dissolve
                            "Kamu mengintip dari balik akar. Peri itu sedang meracik ramuan jiwa di dalam kuali."
                            menu:
                                "Dobrak masuk untuk mencuri":
                                    $ endings_unlocked.add("Ending 3: Kutukan Katak Rawa")
                                    npc "Lancang sekali kau mengotori tempat suci ini!"
                                    "(TAKDIR 3 TERBUKA): Kamu ketahuan dan dikutuk menjadi katak rawa hingga mati!"
                                    jump player_death_cycle

                                "Catat resepnya diam-diam":
                                    $ gold += 200
                                    $ endings_unlocked.add("Ending 4: Pencuri Resep Rahasia")
                                    $ gates_cleared.add(1)
                                    show screen popup_stat("+200 Gold!", "#ffd32a")
                                    sys "(TAKDIR 4 TERBUKA): Resep rahasia berhasil disalin dan ditukar senilai +200 Gold!"
                                    jump sanctuary_hub

        "Ikuti jalan setapak penuh tulang":
            "Kamu tiba di depan gua lembap yang menjadi sarang Monster Slime Raksasa pemakan bangkai!"
            menu:
                "Serang Slime secara langsung":
                    call start_combat("Slime Raksasa", 65, 25, 100, 1)
                    $ endings_unlocked.add("Ending 6: Pembasmi Slime")
                    $ gates_cleared.add(1)
                    sys "(TAKDIR 6 TERBUKA): Slime Raksasa berhasil ditebas habis!"
                    jump sanctuary_hub

                "Sembunyi di balik batu besar":
                    $ endings_unlocked.add("Ending 7: Penyintas Bayangan")
                    $ gates_cleared.add(1)
                    sys "(TAKDIR 7 TERBUKA): Slime melewati tempat persembunyianmu. Kamu kembali dengan selamat."
                    jump sanctuary_hub

# --- WILAYAH 2: LEMBAH LAHAR ---
label gate_2_lava:
    scene bg lava at cg_dramatic_zoom with dissolve
    show npc at center_breathe with dissolve
    "Kamu tiba di Lembah Lahar yang dipenuhi batuan membara dan hujan abu."
    "Di ujung jembatan batu, sosok Raja Iblis berdiri menantangmu!"

    menu:
        "Lawan Raja Iblis demi kehormatan":
            "Raja Iblis mengayunkan pedang apinya!"
            call start_combat("Raja Iblis Lahar", 180, 55, 400, 2)
            $ endings_unlocked.add("Ending 10: Penakluk Raja Iblis")
            $ gates_cleared.add(2)
            sys "(TAKDIR 10 TERBUKA): Melawan takdir kematian, kamu justru berhasil menumbangkan sang Raja Iblis!"
            jump sanctuary_hub

        "Tawarkan perdamaian dan negosiasi bisnis":
            npc "Hmm? Kau tidak mencabut pedangmu? Jujur saja, aku bosan bertarung ribuan tahun di kawah ini."
            "Raja Iblis ternyata kesepian dan menawarkan kerja sama."
            menu:
                "Terima tawaran bisnis tambang batu bara neraka":
                    $ gold += 1000
                    $ endings_unlocked.add("Ending 8: Konglomerat Neraka")
                    $ gates_cleared.add(2)
                    show screen popup_stat("+1000 Gold!", "#ffd32a")
                    sys "(TAKDIR 8 TERBUKA): Investasi batu bara meledak! Kamu mendapat +1000 Gold!"
                    jump sanctuary_hub

                "Tolak bisnisnya dan ajak bermain catur":
                    $ world_peace_chess = True
                    $ remnant_shards += 2
                    $ endings_unlocked.add("Ending 9: Skakmat Perdamaian")
                    $ gates_cleared.add(2)
                    show screen popup_stat("+2 Memory Shards!", "#70a1ff")
                    npc "Skakmat... Kau hebat juga, manusia. Ambil pecahan jiwa ini, aku tidak akan menyerang duniamu lagi."
                    sys "(TAKDIR 9 TERBUKA): Kamu menang catur melawan Raja Iblis dan mendapat +2 Pecahan Memori!"
                    jump sanctuary_hub

# --- WILAYAH 3: BUKIT ANGIN ---
label gate_3_wind:
    scene bg wind at cg_dramatic_zoom with dissolve
    "Kamu mendaki Bukit Angin yang diterpa badai petir. Di puncaknya, sebilah pedang legendaris tertancap di batu altar."

    menu:
        "Cabut pedang sekuat tenaga":
            if max_hp >= 125 or lilith_affection >= 40:
                if "Pedang Excalibur" not in inventory_weapons:
                    $ inventory_weapons.append("Pedang Excalibur")
                $ senjata = "Pedang Excalibur"
                $ endings_unlocked.add("Ending 11: Sang Pemilik Excalibur")
                $ gates_cleared.add(3)
                show screen popup_stat("Senjata Baru: Excalibur!", "#70a1ff")
                sys "(TAKDIR 11 TERBUKA): Berhasil! Kamu mencabut 'Pedang Excalibur' (ATK 65 | DEF 15)!"
                jump sanctuary_hub
            else:
                $ hp -= 40
                show screen popup_stat("-40 HP!", "#ff4757")
                with hpunch
                "Kilatan petir menyambar tubuhmu! Tubuhmu atau ikatan jiwamu belum cukup kuat untuk menahan beban Excalibur."
                sys "Petunjuk: Tingkatkan Max HP di Sanctuary (>=125) atau naikkan Affection Lilith (>=40) untuk mencabutnya!"
                if hp <= 0:
                    jump player_death_cycle
                jump sanctuary_hub

        "Duduk santai menikmati pemandangan di tepi tebing":
            $ endings_unlocked.add("Ending 12: Diterbangkan Badai")
            "(TAKDIR 12 TERBUKA): Angin topan mendadak meniupmu jatuh ke dasar jurang yang tak berujung!"
            jump player_death_cycle

# --- WILAYAH 4: GURUN PASIR ---
label gate_4_desert:
    scene bg desert at cg_dramatic_zoom with dissolve
    "Kamu berjalan di Gurun Pasir yang gersang di bawah matahari hitam dan melihat sebuah oase."

    menu:
        "Langsung minum air oase karena kehausan":
            $ hp -= 50
            show screen popup_stat("Keracunan! -50 HP!", "#ff4757")
            with hpunch
            $ endings_unlocked.add("Ending 13: Oase Beracun")
            $ gates_cleared.add(4)
            "(TAKDIR 13 TERBUKA): Airnya mengandung racun bangkai! HP berkurang 50. Kamu merangkak kembali ke Sanctuary."
            if hp <= 0:
                jump player_death_cycle
            jump sanctuary_hub

        "Periksa airnya terlebih dahulu dengan teliti":
            $ gold += 100
            $ remnant_shards += 1
            $ endings_unlocked.add("Ending 14: Harta Terkubur Oase")
            $ gates_cleared.add(4)
            show screen popup_stat("+100 Gold | +1 Shard!", "#ffd32a")
            sys "(TAKDIR 14 TERBUKA): Kamu menyadari airnya beracun dan justru menemukan peti di dasar pasir berisi 100 Gold & 1 Shard!"
            jump sanctuary_hub

# --- WILAYAH 5: GUNUNG ES ---
label gate_5_ice:
    scene bg ice at cg_dramatic_zoom with dissolve
    "Kamu mendaki Gunung Es Abadi dan melihat seekor anak naga es terjebak di bawah runtuhan gletser."

    menu:
        "Selamatkan anak naga tersebut (-20 HP)":
            $ hp -= 20
            if hp <= 0:
                jump player_death_cycle
            $ remnant_shards += 2
            $ gold += 150
            $ endings_unlocked.add("Ending 15: Balas Budi Sang Naga")
            $ gates_cleared.add(5)
            show screen popup_stat("+150 Gold | +2 Shards!", "#70a1ff")
            "(TAKDIR 15 TERBUKA): Induk naga turun dari langit, memberimu 2 Pecahan Memori dan 150 Gold, lalu mengantarmu terbang pulang!"
            jump sanctuary_hub

        "Biarkan saja dan terus berjalan":
            $ endings_unlocked.add("Ending 16: Membeku di Puncak")
            "(TAKDIR 16 TERBUKA): Badai salju kutukan menerjang mendadak. Tubuhmu membeku menjadi patung es!"
            jump player_death_cycle

# --- WILAYAH 6: TELUK BAJAK LAUT ---
label gate_6_pirate:
    scene bg pirate at cg_dramatic_zoom with dissolve
    "Kamu tiba di Teluk Bajak Laut yang diselimuti kabut hantu. Sebuah kapal galiung besar tampak bersandar."

    menu:
        "Menyelinap masuk ke ruang kapten secara diam-diam":
            $ gold += 300
            $ endings_unlocked.add("Ending 17: Pencuri Harta Bajak Laut")
            $ gates_cleared.add(6)
            show screen popup_stat("+300 Gold!", "#ffd32a")
            sys "(TAKDIR 17 TERBUKA): Kamu berhasil menggasak peti harta karun bajak laut! Gold +300."
            jump sanctuary_hub

        "Mengajak Kapten dan kru kapal bertarung terbuka":
            "Kapten tengkorak beserta puluhan krunya mengepungmu!"
            if WEAPON_DB[senjata]["atk"] >= 45:
                call start_combat("Kapten Bajak Laut Hantu", 140, 40, 350, 1)
                $ endings_unlocked.add("Ending 18B: Pembantai Bajak Laut")
                $ gates_cleared.add(6)
                sys "(TAKDIR 18B TERBUKA): Dengan senjata kuatmu, kamu membabat habis kru hantu dan merebut kapal mereka!"
                jump sanctuary_hub
            else:
                $ endings_unlocked.add("Ending 18: Umpan Hiu Laut Dalam")
                "(TAKDIR 18 TERBUKA): Senjatamu terlalu lemah! Kamu kalah jumlah dan dilempar ke laut menjadi makanan hiu."
                jump player_death_cycle

# --- WILAYAH 7: KASTIL TUA ---
label gate_7_castle:
    scene bg castle at cg_dramatic_zoom with dissolve
    "Kamu menjelajahi Kastil Tua yang terbengkalai. Di lorong utama, berdiri zirah ksatria kosong yang memegang perisai bercahaya."

    menu:
        "Langsung ambil dan pakai perisai itu":
            if "Aegis Shield" not in inventory_weapons:
                $ inventory_weapons.append("Aegis Shield")
            $ senjata = "Aegis Shield"
            $ endings_unlocked.add("Ending 19: Pelindung Aegis")
            $ gates_cleared.add(7)
            show screen popup_stat("Senjata Baru: Aegis Shield!", "#70a1ff")
            sys "(TAKDIR 19 TERBUKA): Perisai magis 'Aegis Shield' (ATK 30 | DEF 45) menyatu denganmu. Pertahananmu tak tertembus!"
            jump sanctuary_hub

        "Ketuk zirah tersebut untuk memastikan":
            "Mata di balik helm besi itu menyala merah! Zirah itu hidup dan mengayunkan gada besinya!"
            $ hp -= 40
            show screen popup_stat("-40 HP!", "#ff4757")
            with hpunch
            if hp <= 0:
                $ endings_unlocked.add("Ending 20: Hancur Dihantam Zirah")
                jump player_death_cycle
            call start_combat("Zirah Hantu Kuno", 110, 35, 250, 1)
            $ endings_unlocked.add("Ending 20: Penakluk Ksatria Hantu")
            $ gates_cleared.add(7)
            sys "(TAKDIR 20 TERBUKA): Meski sempat dihantam keras, kamu berhasil menghancurkan zirah kutukan tersebut!"
            jump sanctuary_hub

# --- WILAYAH 8: RAWA MISTERI ---
label gate_8_swamp:
    scene bg swamp at cg_dramatic_zoom with dissolve
    show npc at center_breathe with dissolve
    "Kamu berjalan di Rawa Misteri yang dipenuhi lumpur isap. Seorang nenek sihir bungkuk muncul dan menawarkan apel berwarna ungu pekat."

    menu:
        "Makan apel ungu itu tanpa ragu":
            $ max_hp += 50
            $ hp += 50
            $ endings_unlocked.add("Ending 21: Berkah Apel Rawa")
            $ gates_cleared.add(8)
            show screen popup_stat("Max HP +50!", "#2ed573")
            sys "(TAKDIR 21 TERBUKA): Apel ajaib! Darah dan batas Maksimal HP kamu meningkat drastis (+50 Max HP)!"
            jump sanctuary_hub

        "Tolak dengan sopan":
            $ endings_unlocked.add("Ending 22: Kutukan Kecoak Rawa")
            npc "Berani-beraninya kau menolak pemberianku, bocah?!"
            "(TAKDIR 22 TERBUKA): Nenek sihir tersinggung lalu mengutuk tubuhmu menyusut menjadi seekor kecoak dan menginjakmu!"
            jump player_death_cycle

# --- WILAYAH 9: KOTA LANGIT ---
label gate_9_sky:
    scene bg sky at cg_dramatic_zoom with dissolve
    show npc at center_breathe with dissolve
    "Kamu menaiki tangga awan berkilau dan tiba di depan gerbang Kota Langit yang megah. Penjaga bersayap meminta tiket emas."

    menu:
        "Coba menyuap penjaga dengan cerita sedih tentang Lilith":
            $ gold += 150
            $ lilith_affection += 10
            $ endings_unlocked.add("Ending 23: Belas Kasih Penjaga Langit")
            $ gates_cleared.add(9)
            show screen popup_stat("+150 Gold | Affection +10!", "#ffd32a")
            npc "Kisah cintamu di dunia yang hancur ini sungguh menyedihkan... Ambillah modal emas ini untuk membahagiakan gadis itu."
            sys "(TAKDIR 23 TERBUKA): Penjaga memberimu +150 Gold dan mendoakan ikatanmu (+10 Affection)!"
            jump sanctuary_hub

        "Nekat melompat melewati pagar gerbang awan":
            $ endings_unlocked.add("Ending 24: Jatuh dari Surga")
            "(TAKDIR 24 TERBUKA): Pijakan awan ternyata ilusi! Kamu terpeleset dan jatuh bebas ribuan meter menghantam bumi."
            jump player_death_cycle

# --- WILAYAH 10: DASAR SAMUDRA ---
label gate_10_ocean:
    scene bg ocean at cg_dramatic_zoom with dissolve
    "Kamu menyelam ke Dasar Samudra yang gelap gulita. Di depan reruntuhan kuil Atlantis, naga air raksasa Leviathan sedang tertidur menjaga sebilah tombak."

    menu:
        "Tantang Dewa Laut Leviathan untuk merebut Tombak Abyssal":
            call start_combat("Dewa Laut Leviathan", 250, 65, 500, 3)
            if "Tombak Abyssal" not in inventory_weapons:
                $ inventory_weapons.append("Tombak Abyssal")
            $ senjata = "Tombak Abyssal"
            $ endings_unlocked.add("Ending 25: Penguasa Samudra Abyss")
            $ gates_cleared.add(10)
            show screen popup_stat("Senjata Baru: Tombak Abyssal!", "#70a1ff")
            sys "(TAKDIR 25 TERBUKA): Leviathan tumbang! Kamu memperoleh senjata terkuat 'Tombak Abyssal' (ATK 85 | DEF 25)!"
            jump sanctuary_hub

        "Ambil mutiara bercahaya di dekat ekornya lalu kabur perlahan":
            $ gold += 250
            $ remnant_shards += 1
            $ endings_unlocked.add("Ending 26: Penyelam Hening")
            $ gates_cleared.add(10)
            show screen popup_stat("+250 Gold | +1 Shard!", "#ffd32a")
            sys "(TAKDIR 26 TERBUKA): Tanpa membangunkan sang monster, kamu membawa pulang mutiara senilai 250 Gold & 1 Shard!"
            jump sanctuary_hub