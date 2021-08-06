import pandas as pd
import folium

#데이터 불러오기
daegu = pd.read_csv('대구시_어린이_보호구역.csv', encoding = 'utf-8')
daegu_child_accident = pd.read_csv('대구시_어린이_교통사고_발생건수.csv', encoding='utf-8')

location_info = daegu[['주소', '위도', '경도']]
child_accident = daegu_child_accident[['연도', '주소', '위도', '경도', '발생빈도', '구', '동']]

print(child_accident)
map = folium.Map(location = [35.8223377900372,128.53066522102513], zoom_start = 16.5)

for a in location_info.index:
    latitude = location_info.loc[a,"위도"]
    longtitude = location_info.loc[a,"경도"]
    tooltip = location_info.loc[a,"주소"]
    folium.Circle([latitude, longtitude], radius=200, color='#fcdf03', fill_color='#fcdf03', popup='<i>어린이 보호구역(반경 200M)</i>', tooltip =tooltip).add_to(map) 

for row in child_accident.index:
    latitude = child_accident.loc[row, "위도"]
    longtitude = child_accident.loc[row,"경도"]
    tooltip = child_accident.loc[row,"주소"]

    table_test = '<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>CSS</title><style>table{width:100%}</style></head><body><table><tbody><tr><td>사고연도</td><td>' + str(child_accident.loc[row, "연도"]) + '</td></tr><tr><td>발생빈도</td><td>' + str(child_accident.loc[row, "발생빈도"]) + '</td></tr><tr><td>주소</td><td>' + child_accident.loc[row, "주소"] + '</td></tr><tr><td>구</td><td>' + child_accident.loc[row, "구"] + '</td></tr><tr><td>동</td><td>' + child_accident.loc[row, "동"] + '</td></tr></tbody></table></body></html><style>table{width:100%;border-top:1px solid#444444;border-collapse:collapse}th,td{border-bottom:1px solid#444444;padding:10px}</style>'
    popup_info = '<b>주소</b>: ' + child_accident.loc[row, "주소"] + '<br>' + '<b>연도</b>: ' + str(child_accident.loc[row, "연도"]) + '<br>' + '<b>발생빈도</b>: ' + str(child_accident.loc[row,"발생빈도"]) + '<br>' + '<b>구</b>: ' + child_accident.loc[row, '구'] + '<br>' + '<b>동</b>: ' + child_accident.loc[row, '동']
    
    iframe = folium.IFrame(table_test, width=400, height=150)
    popup = folium.Popup(iframe, max_width=500)
    folium.Marker([latitude, longtitude], tooltip=tooltip, popup=popup).add_to(map)

map.save("index.html")