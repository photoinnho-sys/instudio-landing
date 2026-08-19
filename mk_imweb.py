# -*- coding: utf-8 -*-
"""데모(사진 내장) → 아임웹 삽입용(사진 CDN 주소) 자동 변환.
   두 파일이 어긋나지 않도록 항상 이 스크립트로 생성한다."""
import base64, os, re
M = {  # 아임웹 CDN 파일명 → 로컬 데모 파일
 'd40420412f1a0.jpg':'11_내동집.jpg','b5b5a5a337805.jpg':'03_로바타야키토라.jpg',
 'a7c335f1000ce.jpg':'09_피자스팟.jpg','fc7fce5a5e98d.jpg':'05_샐러드마비에_한상.jpg',
 'fe9ad2186a0a8.jpeg':'02_지누스.jpeg','92189e3d29d28.jpg':'17_구전국밥_외관.jpg',
 'ae6ad68a237b3.jpg':'01_더본코리아_볶음밥.jpg','aa9b22cc64cf1.jpg':'04_샐러드마비에_건물.jpg',
 'b8292aa85bf60.jpg':'06_삼성RND_프로필.jpg','2b57924037618.jpg':'08_롯데유통군.jpg',
 '5e9182fec29ca.jpg':'26_노이즈냅.jpg','d488781c2c742.jpg':'30_압토스심포지엄.jpg'}
rev={}
for cdn, local in M.items():
    b=base64.b64encode(open(os.path.join('demoimg',local),'rb').read()).decode()
    rev['data:image/jpeg;base64,'+b] = 'https://cdn.imweb.me/thumbnail/20260819/'+cdn

s=open('index.html',encoding='utf-8').read()
n=0
for data,url in rev.items():
    if data in s:
        s=s.replace(data,url); n+=1
# 폰트는 내장 유지(외부 요청 0 = 더 빠름). 남은 data:image 가 있으면 경고
left=len(re.findall(r'data:image/', s))
open('dist/imweb.html','w',encoding='utf-8').write(s)
print("이미지 %d종 → CDN 주소로 치환 · 남은 내장이미지 %d" % (n, left))
print("아임웹용 파일 크기: %.0f KB" % (len(s)/1024))
