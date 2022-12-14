from app.models import Status

try:
    
    # create statuses
    status = Status.objects.filter(code = 'in stock').first()
    if not status:
        status = Status(code = 'in stock', name = "В наличии") 
        status.save()
    status = Status.objects.filter(code = 'Under the order').first()
    if not status:
        status = Status(code = 'Under the order', name = "Под заказ") 
        status.save()
    status = Status.objects.filter(code = 'Delivery is expected').first()
    if not status:
        status = Status(code = 'Delivery is expected', name = "Ожидается поступление") 
        status.save()
    status = Status.objects.filter(code = 'Out of stock').first()
    if not status:
        status = Status(code = 'Out of stock', name = "Нет в наличии") 
        status.save()
    status = Status.objects.filter(code = 'Not produced').first()
    if not status:
        status = Status(code = 'Not produced', name = "Не производится") 
        status.save()

except:
    pass 