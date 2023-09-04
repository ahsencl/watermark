from PIL import Image, ImageDraw, ImageFont
import json


def load_sconfig(sconfig_path):
    with open(sconfig_path, 'r') as sconfig_file:
        sconfig = json.load(sconfig_file)
        return sconfig


def add_system_info(sconfig):
    main_image = Image.open(sconfig["main_image_path"])
    systeminfo = Image.new("RGBA", main_image.size,
                           (0, 0, 0, 0))  # Asıl resimle aynı boyutlarda resmin üstüne sayfım bir sayfa
    draw = ImageDraw.Draw(systeminfo)  # sayfa üzerine çizim yapmak için  çizim nesnesi
    text_color = tuple(sconfig["color"])  # Metin rengini verme
    font = ImageFont.truetype('arial.ttf', sconfig["font_size"])  # yazı tipi ve boyut verme
    draw.text(sconfig["position"], sconfig["text"], font=font, fill=tuple(text_color))  # Metni sayfa üzerine çiz
    main_image.paste(systeminfo, (0, 0), systeminfo)  # resmin üzerine oluşturğun sayfayı koy
    main_image.save(sconfig["output_path"])  # çıktıyı dosyaya kaydet

    print("BAŞARILI:", sconfig["output_path"])


if __name__ == "__main__":
    sconfig = load_sconfig("sconfig.json")
    add_system_info(sconfig)