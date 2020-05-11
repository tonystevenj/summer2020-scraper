import requests
from PIL import Image
from io import BytesIO
import re

headers = {
    # 假装自己是浏览器
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36',
    # 把你刚刚拿到的Cookie塞进来
    'Cookie': '__cfduid=d4029488e26da907c4da3fa88b33ccc141588816713; first_visit_datetime_pc=2020-05-07+10%3A58%3A34; p_ab_id=3; p_ab_id_2=8; p_ab_d_id=1372031937; yuid_b=MHZ5mZY; __utma=235335808.633421846.1588816718.1588816718.1588816718.1; __utmc=235335808; __utmz=235335808.1588816718.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; login_bc=1; PHPSESSID=33232702_rGhpD4KQUKkDk2Lr2mb3Ufnj2VPDaYhF; device_token=586a5b4224abb231b2b61ef7899a090d; c_type=25; privacy_policy_agreement=2; a_type=0; b_type=1; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=33232702=1^9=p_ab_id=3=1^10=p_ab_id_2=8=1^11=lang=zh=1; __gads=ID=d549866be679108c:T=1588816743:S=ALNI_MZ9vJ-4l5SEWuq9KVhSlp8kVoDV9w; _fbp=fb.1.1588816745007.1892111677; module_orders_mypage=%5B%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; is_sensei_service_user=1; ki_t=1588816807822%3B1588816807822%3B1588816807822%3B1%3B1; ki_r=; _ga=GA1.2.633421846.1588816718; _gid=GA1.2.267831662.1588816871; _gat_UA-1830249-3=1; __utmb=235335808.9.9.1588816801078',
}
url = "https://www.pixiv.net/artworks/81193827"


session = requests.Session()
response = session.get(url)
# print(response.text)
begin = re.search("original", response.text)
end = re.search("tags", response.text)
temurl = response.text[begin.span()[0]:end.span()[0]]
begin1=temurl.index("http")
end1 = temurl.index("jpg")+3
print(temurl[begin1:end1])

headers['referer'] = url
response = requests.get(temurl[begin1:end1],headers=headers)
image = Image.open(BytesIO(response.content))
image.show()
image.save('E:\Output2\PixivScrape\80090766.jpg')
# end = re.search(";pixiv.context.illustRecommendZone", response.text)

# print(result.span()[0])
# tem =response.text[begin.span()[0]:end.span()[0]]
# print(tem)
# Ids = re.findall("[0-9]+",tem)
# print(type(Ids))
# print(len(Ids))

exit()

headers = {
    # 假装自己是浏览器
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36',
    # 把你刚刚拿到的Cookie塞进来
    'Cookie': '__cfduid=d4029488e26da907c4da3fa88b33ccc141588816713; first_visit_datetime_pc=2020-05-07+10%3A58%3A34; p_ab_id=3; p_ab_id_2=8; p_ab_d_id=1372031937; yuid_b=MHZ5mZY; __utma=235335808.633421846.1588816718.1588816718.1588816718.1; __utmc=235335808; __utmz=235335808.1588816718.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; login_bc=1; PHPSESSID=33232702_rGhpD4KQUKkDk2Lr2mb3Ufnj2VPDaYhF; device_token=586a5b4224abb231b2b61ef7899a090d; c_type=25; privacy_policy_agreement=2; a_type=0; b_type=1; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=33232702=1^9=p_ab_id=3=1^10=p_ab_id_2=8=1^11=lang=zh=1; __gads=ID=d549866be679108c:T=1588816743:S=ALNI_MZ9vJ-4l5SEWuq9KVhSlp8kVoDV9w; _fbp=fb.1.1588816745007.1892111677; module_orders_mypage=%5B%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; is_sensei_service_user=1; ki_t=1588816807822%3B1588816807822%3B1588816807822%3B1%3B1; ki_r=; _ga=GA1.2.633421846.1588816718; _gid=GA1.2.267831662.1588816871; _gat_UA-1830249-3=1; __utmb=235335808.9.9.1588816801078',
}
session = requests.Session()
response = session.get('https://www.pixiv.net/bookmark.php?rest=show&p=1', headers=headers)
# print(response.text)
begin = re.search("illustRecommendSampleIllust", response.text)
end = re.search(";pixiv.context.illustRecommendZone", response.text)

# print(result.span()[0])
tem =response.text[begin.span()[0]:end.span()[0]]
print(tem)
Ids = re.findall("[0-9]+",tem)
print(type(Ids))
print(len(Ids))