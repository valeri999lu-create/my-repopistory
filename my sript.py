oridjory=34605 # калькулятор для гача игры на 80 поптыке тебе падает какойто легендарный персонаж
tiket=0        #  на 120 попытке тебе падает нужный
total=int(oridjory/500+tiket)
if total<=69:
    print(total,"плохая  идея")
elif total>69 and total<120:
        print(total, "удачи на все воля кубика")
else:
    print( total," гарант есть")
