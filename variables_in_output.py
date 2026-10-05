# old
age = 23 
print("I am %d years old" % (age)) # %d for int, %s for str, and %f for float (you can add limits for floats, e.g. %.3f)
print("________________________________________________________")
name = 'Keivan'
age = 19
height = 1.81121121
print('%s is %d years old. His height is %.2f m.' % (name, age, height)) 
print("________________________________________________________")
print("%03d" % (2)) # 002 , this is called padding 
print("________________________________________________________")
name = "Keivan"
age = 18
print("{} is {} years old".format(name, age))
print("________________________________________________________")
name = "Keivan"
age = 19

print(f"Hello, my name is {name} and I am {age} years old.") # The {} in f-string isn't just for putting variables! Python computes every code you write in {} first, then puts the result in the text. 
print("________________________________________________________")
side = 4
# محاسبه مساحت مستقیم داخل آکولاد انجام می‌شود
print(f"Area of square with side {side} is {side * side}.")
print("________________________________________________________")
# می‌توانید توابع پایتون را مستقیم روی متغیرها داخل {} اعمال کنید:
name = "ali"
# تبدیل حرف اول به بزرگ با تابع capitalize
print(f"Welcome, {name.capitalize()}!")
print("________________________________________________________")
''' گاهی می‌خواهیم فرمت نمایش اعداد را تغییر دهیم (مثلاً تعداد ارقام اعشار را محدود کنیم). در f-string برای این کار، بعد از نام متغیر یک دو نقطه (:) می‌گذاریم و الگوی فرمت را می‌نویسیم:

    فرمول کلی: {متغیر:فرمت}

'''
pi = 3.14159265

# چاپ تا ۲ رقم اعشار
print(f"Pi up to 2 decimal places: {pi:.2f}")

# چاپ تا ۴ رقم اعشار
print(f"Pi up to 4 decimal places: {pi:.4f}")
print("________________________________________________________")
'''پر کردن پشت عدد با صفر (Padding با :0xd)

اگر بخواهیم یک عدد صحیح حتماً یک طول مشخص (مثلاً ۳ رقم) داشته باشد و اگر کمتر بود با صفر پر شود، از فرمت :0xd استفاده می‌کنیم (که d تعداد کل ارقام است):'''
day = 5
month = 9
print(f"Date: {month:02d}/{day:02d}") #Date: 09/05
# در روش % نوشتن d الزامی بود (%03d)، اما در f-string نوشتن d بعد از پدینگ اختیاری است (یعنی {month:02} و {month:02d} هر دو یک کار را انجام می‌دهند).
