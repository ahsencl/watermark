from PIL import Image, ImageDraw, ImageFont
import json


def load_config(config_path):
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
        return config


def add_text_watermark(config):   #config den alınan veriler ile;

    main_image = Image.open(config["main_image_path"])
    watermark = Image.new("RGBA", main_image.size, (0, 0, 0, 0))   #Asıl resimle aynı boyutlarda resmin üstüne sayfım bir sayfa
    draw = ImageDraw.Draw(watermark)    #sayfa üzerine çizim yapmak için  çizim nesnesi
    text_color = tuple(config["color"])     # Metin rengini verme
    font = ImageFont.truetype('arial.ttf', config["font_size"])   # yazı tipi ve boyut verme
    draw.text(config["position"], config["text"], font=font, fill=tuple(text_color))   # Metni sayfa üzerine çiz
    main_image.paste(watermark, (0, 0), watermark)  # resmin üzerine oluşturğun sayfayı koy
    main_image.save(config["output_path"])  #çıktıyı dosyaya kaydet

    print("BAŞARILI:", config["output_path"])

if __name__ == "__main__":
    config = load_config("config.json")
    add_text_watermark(config)
