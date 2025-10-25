import time
from colorama import init, Fore

# مقداردهی اولیه Colorama
init(autoreset=True)

# طراحی ABOL BLACK با حروف بزرگ
text = [
    "   AAAAA    BBBB   OOO     BBBB    L      AAAAA    CCCC   K  K",
    "  A     A   B   B O   O   B   B   L     A     A  C      K K ",
    "  AAAAAAA   BBBB  O   O   BBBB    L     AAAAAAA  C      KK  ",
    "  A     A   B   B O   O   B   B   L     A     A  C      K K ",
    "  A     A   BBBB   OOO    BBBB    LLLLL A     A   CCCC   K  K"
]

# نمایش طراحی ABOL BLACK به رنگ سبز
for line in text:
    for char in line:
        print(Fore.GREEN + char, end='', flush=True)
        time.sleep(0.05)  # خواب 0.05 ثانیه بین هر کاراکتر
    print()  # رفتن به خط بعدی
    time.sleep(0.5)  # خواب 0.5 ثانیه بین هر خط

# نمایش متن "ALI RAISON AND GADAF SHAH"
message = "(ABOL BLACK)"
for char in message:
    print(Fore.GREEN + char, end='', flush=True)
    time.sleep(0.1)  # خواب 0.1 ثانیه بین هر کاراکتر
print()  # رفتن به خط بعدی






import os
from PIL import Image, ImageDraw, ImageFont

# مسیر پوشه برای ذخیره تصویر
folder_path = "/storage/emulated/0/سلام"
os.makedirs(folder_path, exist_ok=True)

# --- ورودی‌ها را از کاربر دریافت می‌کنیم ---
binary_input = input("کد باینری ورودی را وارد کنید: ").strip()
desired_text = input("متن واضحی که باید روی عکس نمایش داده شود را وارد کنید: ").strip()
# ------------------------------------------

try:
    # پد کردن (برای حفظ منطق، اگرچه در این حالت استفاده نمی‌شود)
    if len(binary_input) % 8 != 0:
        pad_len = 8 - (len(binary_input) % 8)
        binary_input += "0" * pad_len

    # 1. ساختن تصویر کاملاً سیاه با ابعاد 4K
    fixed_width = 3840
    fixed_height = 2160
    
    # تصویر سیاه (RGB)
    img_rgb = Image.new('RGB', (fixed_width, fixed_height), color = 'black')
    draw = ImageDraw.Draw(img_rgb)
    
    # متن نمایش داده شده
    display_text = f"رمزگشایی نهایی: {desired_text}"

    # 💥 فونت بسیار بزرگ (300) برای رزولوشن 4K و رنگ سفید برای حداکثر کنتراست
    try:
        # سعی می‌کنیم از فونت سیستمی استفاده کنیم
        font = ImageFont.truetype("/system/fonts/DroidSans.ttf", 300)
    except IOError:
        # اگر فونت سفارشی پیدا نشد، از پیش‌فرض استفاده می‌کنیم
        font = ImageFont.load_default()

    # محاسبه موقعیت متن (وسط تصویر)
    bbox = draw.textbbox((0, 0), display_text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    pos_x = (img_rgb.width - text_w) // 2
    pos_y = (img_rgb.height - text_h) // 2
    
    position = (pos_x, pos_y)

    # نوشتن متن با رنگ سفید
    draw.text(position, display_text, fill=(255, 255, 255), font=font) 

    # ذخیره تصویر نهایی
    output_path = os.path.join(folder_path, f"عکس_4K_{desired_text}.png")
    img_rgb.save(output_path)
    
    # نمایش تصویر
    img_rgb.show()

    print(f"✅ تصویر 4K با متن '{desired_text}' با موفقیت ساخته شد و در مسیر زیر ذخیره شد:\n{output_path}")

except Exception as e:
    print(f"[خطا] مشکلی در پردازش پیش آمد: {str(e)}")
