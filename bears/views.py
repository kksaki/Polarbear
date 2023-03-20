from django.shortcuts import render, get_object_or_404    # （如果没有从查询中返回的熊，那么页面就会显示一个404错误信息。）
from .models import Bear #注意这里每个表都要import！！！不要把sighting忘记！
# 生成一个熊的列表：
def bear_list(request):
    bears = Bear.objects.all()
    return render(request, 'bears/bear_list.html', {'bears' : bears})

def females(request):
    females = Bear.female()
    return render(request, 'bears/bear_list.html', {'bears' : females})

def bear_detail(request, id):
    bear = get_object_or_404(Bear, id=id)
    return render(request, 'bears/bear_detail.html', {'bear' : bear})

# def bear_detail(request, id):
#     bear = get_object_or_404(Bear, id=id)
#     sightings = Sighting.objects.filter(bear_id=id)
#     return render(request, 'bears/bear_detail.html', {'bear': bear, 'sightings': sightings})
