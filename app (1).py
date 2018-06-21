from flask import Flask, request, abort

from linebot import (
	LineBotApi, WebhookHandler
)
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot.models import (
	MessageEvent, TextMessage, TextSendMessage,
)
from linebot.models import *
import requests
import sys
import datetime
import pytz
app = Flask(__name__)
tpe = pytz.timezone('Asia/Taipei')
line_bot_api = LineBotApi('line bot Channel access token')
handler = WebhookHandler('line bot Channel secret')
message = TemplateSendMessage(
	alt_text = '天氣資訊',
	template=ButtonsTemplate(
		title='請選擇城市或台灣',
		text='請選擇',
		actions=[
			MessageTemplateAction(
				label='桃園市',
				text='桃園市',
			),
			MessageTemplateAction(
				label='台灣',
				text='台灣',
			),
			MessageTemplateAction(
				label='離島',
				text='離島',
			)
			
		]
	)
)

@app.route("/callback", methods=['POST'])
def callback():
	signature = request.headers['X-Line-Signature']
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)
	return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	profile = line_bot_api.get_profile(event.source.user_id)
	response = requests.get('php-ip'+profile.display_name+'&answer='+event.message.text+'&time='+datetime.datetime.now(tpe).strftime("%Y-%m-%d %H:%M:%S"))
	message1 = TemplateSendMessage(
		alt_text = '桃園市',
		template=ButtonsTemplate(
			title='請選擇想要地區資料',
			text='請選擇',
			actions=[
				MessageTemplateAction(
					label='完整天氣資訊',
					text='完整天氣資訊',
				),
				MessageTemplateAction(
					label='氣溫',
					text='氣溫',
				),
				MessageTemplateAction(
					label='降雨機率',
					text='降雨機率',
				)
			]
		)
	)
	message11 = TemplateSendMessage(
		alt_text = '台灣',
		template=ButtonsTemplate(
			title='請選擇想要地區',
			text='請選擇',
			actions=[
				MessageTemplateAction(
					label='北台灣',
					text='北台灣',
				),
				MessageTemplateAction(
					label='中台灣',
					text='中台灣',
				),
				MessageTemplateAction(
					label='南台灣',
					text='南台灣',
				),
				MessageTemplateAction(
					label='東台灣',
					text='東台灣',
				)
			]
		)
	)
	message2=TemplateSendMessage(
		alt_text = '完整天氣資訊',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='中壢區',
					text='中壢區',
					actions=[
						URITemplateAction(
							label='中壢區資訊',
							uri='https://drive.google.com/file/d/1t3j_mjSRn93TN_WK5hgROVvLbVkVHjMO/view?usp=sharing'+profile.display_name+'&information=中壢區'
						)
					]
				),
				CarouselColumn(
					title='蘆竹區',
					text='蘆竹區',
					actions=[
						URITemplateAction(
							label='蘆竹區資訊',
							uri='https://drive.google.com/file/d/1yXwARY9hTU-uUKsPKTzym71qQiDrv790/view?usp=sharing'+profile.display_name+'&information=蘆竹區'
						)
					]
				),
				CarouselColumn(
					title='觀音區',
					text='觀音區',
					actions=[
						URITemplateAction(
							label='觀音區資訊',
							uri='https://drive.google.com/file/d/1-MPO931l2o7GT49BBOvPnKj1B_VgbSa2/view?usp=sharing'+profile.display_name+'&information=觀音區'
						)
					]
				),
				CarouselColumn(
					title='龜山區',
					text='龜山區',
					actions=[
						URITemplateAction(
							label='龜山區資訊',
							uri='https://drive.google.com/file/d/1kemUzt_FiBvM5_P1IHexpuh1tSLC4f2T/view?usp=sharing'+profile.display_name+'&information=龜山區'
						)
					]
				),
				CarouselColumn(
					title='楊梅區',
					text='楊梅區',
					actions=[
						URITemplateAction(
							label='楊梅區資訊',
							uri='https://drive.google.com/file/d/1SWYG8DpS_1u2e0nr7QLzNosIoJeHHR94/view?usp=sharing'+profile.display_name+'&information=楊梅區'
						)
					]
				),
				CarouselColumn(
					title='龍潭區',
					text='龍潭區',
					actions=[
						URITemplateAction(
							label='龍潭區資訊',
							uri='https://drive.google.com/file/d/1vhEYQxo9L3iBuTJNPJPBdvjQiHVm5J6F/view?usp=sharing'+profile.display_name+'&information=龍潭區'
						)
					]
				),
				CarouselColumn(
					title='大園區',
					text='大園區',
					actions=[
						URITemplateAction(
							label='大園區資訊',
							uri='https://drive.google.com/file/d/1aMEkmL_awxiRoxPLBKiYpF9dNM4ZXTc2/view?usp=sharing'+profile.display_name+'&information=大園區'
						)
					]
				),
				CarouselColumn(
					title='平鎮區',
					text='平鎮區',
					actions=[
						URITemplateAction(
							label='八德區資訊',
							uri='https://drive.google.com/file/d/1_Bvi-FuKo-TFkOGUaXd-JKH-TyiGwNEb/view?usp=sharing'+profile.display_name+'&information=平鎮區'
						)
					]
				)
				
			]
		)
	)
	message3=TemplateSendMessage(
		alt_text = '完整天氣資訊',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='大溪區',
					text='大溪區',
					actions=[
						URITemplateAction(
							label='大溪區資訊',
							uri='https://drive.google.com/file/d/177V_caqAqTmJddAva2RhrIdNvSs8iMzN/view?usp=sharing'+profile.display_name+'&information=大溪區'
						)
					]
				),
				CarouselColumn(
					title='桃園區',
					text='桃園區',
					actions=[
						URITemplateAction(
							label='桃園區資訊',
							uri='https://drive.google.com/file/d/12s_nZfz7BeeB06_oasZhKusCvLpgi3m9/view?usp=sharing'+profile.display_name+'&information=桃園區'
						)
					]
				),
				CarouselColumn(
					title='復興區',
					text='復興區',
					actions=[
						URITemplateAction(
							label='復興區資訊',
							uri='https://drive.google.com/file/d/10CJMhIcePMRW6Xcp99e69GMETRoOb-QQ/view?usp=sharing'+profile.display_name+'&information=復興區'
						)
					]
				),
				CarouselColumn(
					title='新屋區',
					text='新屋區',
					actions=[
						URITemplateAction(
							label='新屋區資訊',
							uri='https://drive.google.com/file/d/1l3-1ozlE566MvuSSttunAyjTBanTl_kF/view?usp=sharing'+profile.display_name+'&information=新屋區'
						)
					]
				),
				CarouselColumn(
					title='八德區',
					text='八德區',
					actions=[
						URITemplateAction(
							label='八德區資訊',
							uri='https://drive.google.com/file/d/1ydL8HT9QZU3pc_HnwVTZ8_gwl_ElD2-q/view?usp=sharing'+profile.display_name+'&information=八德區'
						)
					]
				)	
				
			]
		)
	)
	message4=TemplateSendMessage(
		alt_text = '氣溫',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='中壢區',
					text='中壢區',
					actions=[
						URITemplateAction(
							label='中壢區氣溫資訊',
							uri='https://drive.google.com/file/d/1ZCF-DZ_vIyCUJGMEWKBY3PXV9mnGprcB/view?usp=sharing'+profile.display_name+'&information=中壢區'
						)
					]
				),
				CarouselColumn(
					title='蘆竹區',
					text='蘆竹區',
					actions=[
						URITemplateAction(
							label='蘆竹區氣溫資訊',
							uri='https://drive.google.com/file/d/1safxp423FSnA0JrDqOtVU-CCYxOQBN8K/view?usp=sharing'+profile.display_name+'&information=蘆竹區'
						)
					]
				),
				CarouselColumn(
					title='觀音區',
					text='觀音區',
					actions=[
						URITemplateAction(
							label='觀音區氣溫資訊',
							uri='https://drive.google.com/file/d/13q_Dq50k7n9hkSUv3DFfHpAnVghVrmEF/view?usp=sharing'+profile.display_name+'&information=觀音區'
						)
					]
				),
				CarouselColumn(
					title='龜山區',
					text='龜山區',
					actions=[
						URITemplateAction(
							label='龜山區氣溫資訊',
							uri='https://drive.google.com/file/d/105nprk7a_8m4UaMj8-0wbA3-ub_U-c56/view?usp=sharing'+profile.display_name+'&information=龜山區'
						)
					]
				),
				CarouselColumn(
					title='楊梅區',
					text='楊梅區',
					actions=[
						URITemplateAction(
							label='楊梅區氣溫資訊',
							uri='https://drive.google.com/file/d/12uN21K6H5MR4PKwZLnBL1N-vAj4_0Wtb/view?usp=sharing'+profile.display_name+'&information=楊梅區'
						)
					]
				),
				CarouselColumn(
					title='龍潭區',
					text='龍潭區',
					actions=[
						URITemplateAction(
							label='龍潭區氣溫資訊',
							uri='https://drive.google.com/file/d/1nEtAPvlvsmGJZ4jyBaBX2g-dYNBeDmZe/view?usp=sharing'+profile.display_name+'&information=龍潭區'
						)
					]
				),
				CarouselColumn(
					title='大園區',
					text='大園區',
					actions=[
						URITemplateAction(
							label='大園區氣溫資訊',
							uri='https://drive.google.com/file/d/16zuUGErvzdjXFXqcXoQtJfWWIMYfkfiP/view?usp=sharing'+profile.display_name+'&information=大園區'
						)
					]
				),
				CarouselColumn(
					title='平鎮區',
					text='平鎮區',
					actions=[
						URITemplateAction(
							label='平鎮區氣溫資訊',
							uri='https://drive.google.com/file/d/1xqCKjVAqZnLU4oN48xbeMn2TmX7Q0gDg/view?usp=sharing'+profile.display_name+'&information=平鎮區'
						)
					]
				)
				
			]
		)
	)
	message5=TemplateSendMessage(
		alt_text = '氣溫',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='大溪區',
					text='大溪區',
					actions=[
						URITemplateAction(
							label='大溪區氣溫資訊',
							uri='https://drive.google.com/file/d/1_6vuXMU3TcQZSWxB5CVMFSpOvrVEsLn2/view?usp=sharing'+profile.display_name+'&information=大溪區'
						)
					]
				),
				CarouselColumn(
					title='桃園區',
					text='桃園區',
					actions=[
						URITemplateAction(
							label='桃園區氣溫資訊',
							uri='https://drive.google.com/file/d/1wd6x0yShWbXN6jpgiStoxY57HBiZ-NUH/view?usp=sharing'+profile.display_name+'&information=桃園區'
						)
					]
				),
				CarouselColumn(
					title='復興區',
					text='復興區',
					actions=[
						URITemplateAction(
							label='復興區氣溫資訊',
							uri='https://drive.google.com/file/d/1AZN1KZZzEJTBCcXZ4ZGQEHWuT_Ur1d8W/view?usp=sharing'+profile.display_name+'&information=復興區'
						)
					]
				),
				CarouselColumn(
					title='新屋區',
					text='新屋區',
					actions=[
						URITemplateAction(
							label='新屋區氣溫資訊',
							uri='https://drive.google.com/file/d/1AVAVeqCKcqFWhXFxfHx-vKHtB01Vrk7b/view?usp=sharing'+profile.display_name+'&information=新屋區'
						)
					]
				),
				CarouselColumn(
					title='八德區',
					text='八德區',
					actions=[
						URITemplateAction(
							label='八德區氣溫資訊',
							uri='https://drive.google.com/file/d/1UGNBgWkLIueM7JiBkhsMTV4UFiZsIT3S/view?usp=sharing'+profile.display_name+'&information=八德區'
						)
					]
				)	
				
			]
		)
	)
	message6=TemplateSendMessage(
		alt_text = '降雨機率',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='中壢區',
					text='中壢區',
					actions=[
						URITemplateAction(
							label='中壢區降雨資訊',
							uri='https://drive.google.com/file/d/1aV8EVKTLZBeHqNazTicmOhweq-rK7Cre/view?usp=sharing'+profile.display_name+'&information=中壢區'
						)
					]
				),
				CarouselColumn(
					title='蘆竹區',
					text='蘆竹區',
					actions=[
						URITemplateAction(
							label='蘆竹區降雨資訊',
							uri='https://drive.google.com/file/d/1bi-jUZ7CQfQqwGN4VTUKOTJ5DrkR4dwt/view?usp=sharing'+profile.display_name+'&information=蘆竹區'
						)
					]
				),
				CarouselColumn(
					title='觀音區',
					text='觀音區',
					actions=[
						URITemplateAction(
							label='觀音區降雨資訊',
							uri='https://drive.google.com/file/d/1PKbWCULW6I1Mh1otznmIehsmSjSM4M9j/view?usp=sharing'+profile.display_name+'&information=觀音區'
						)
					]
				),
				CarouselColumn(
					title='龜山區',
					text='龜山區',
					actions=[
						URITemplateAction(
							label='龜山區降雨資訊',
							uri='https://drive.google.com/file/d/11KfH76Pz1UEantH3GZbV0djQR7SBS3IM/view?usp=sharing'+profile.display_name+'&information=龜山區'
						)
					]
				),
				CarouselColumn(
					title='楊梅區',
					text='楊梅區',
					actions=[
						URITemplateAction(
							label='楊梅區降雨資訊',
							uri='https://drive.google.com/file/d/1H7HS5HZpJ2O7G0BJkMHK65ltQOLpWBhr/view?usp=sharing'+profile.display_name+'&information=楊梅區'
						)
					]
				),
				CarouselColumn(
					title='龍潭區',
					text='龍潭區',
					actions=[
						URITemplateAction(
							label='龍潭區降雨資訊',
							uri='https://drive.google.com/file/d/1giDmNN9yOWrDdAi9kH4LiTck6f0PERrm/view?usp=sharing'+profile.display_name+'&information=龍潭區'
						)
					]
				),
				CarouselColumn(
					title='大園區',
					text='大園區',
					actions=[
						URITemplateAction(
							label='大園區降雨資訊',
							uri='https://drive.google.com/file/d/1wT5q9XCDUBpMvGmpsa_Sf0CPpkbFMYV8/view?usp=sharing'+profile.display_name+'&information=大園區'
						)
					]
				),
				CarouselColumn(
					title='平鎮區',
					text='平鎮區',
					actions=[
						URITemplateAction(
							label='平鎮區降雨資訊',
							uri='https://drive.google.com/file/d/1tEpZwRTueiSXAsMnayQGQt4jdeiORR-1/view?usp=sharing'+profile.display_name+'&information=平鎮區'
						)
					]
				)
				
			]
		)
	)
	message7=TemplateSendMessage(
		alt_text = '降雨機率',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='大溪區',
					text='大溪區',
					actions=[
						URITemplateAction(
							label='大溪區降雨資訊',
							uri='https://drive.google.com/file/d/19_gI0URvFiqx7UU1hlYxFBhsNFwX-bAu/view?usp=sharing'+profile.display_name+'&information=大溪區'
						)
					]
				),
				CarouselColumn(
					title='桃園區',
					text='桃園區',
					actions=[
						URITemplateAction(
							label='桃園區降雨資訊',
							uri='https://drive.google.com/file/d/14WQIuDj5gtzciD2roKNCmAiDecbPgy8a/view?usp=sharing'+profile.display_name+'&information=桃園區'
						)
					]
				),
				CarouselColumn(
					title='復興區',
					text='復興區',
					actions=[
						URITemplateAction(
							label='復興區降雨資訊',
							uri='https://drive.google.com/file/d/1mub6YQr_OuwnCqFDFMR0YxIs9cxJWACv/view?usp=sharing'+profile.display_name+'&information=復興區'
						)
					]
				),
				CarouselColumn(
					title='新屋區',
					text='新屋區',
					actions=[
						URITemplateAction(
							label='新屋區降雨資訊',
							uri='https://drive.google.com/file/d/182SieN_cZnLQN_Tu1P1IBk-p1SBuwhdc/view?usp=sharing'+profile.display_name+'&information=新屋區'
						)
					]
				),
				CarouselColumn(
					title='八德區',
					text='八德區',
					actions=[
						URITemplateAction(
							label='八德區降雨資訊',
							uri='https://drive.google.com/file/d/1GxKEXL-7_BCYVWpZRi7VbmKPMSsPpdqm/view?usp=sharing'+profile.display_name+'&information=八德區'
						)
					]
				)	
				
			]
		)
	)
	message12 = TemplateSendMessage(
		alt_text = '北台灣',
		template=ButtonsTemplate(
			title='請選擇想要資訊',
			text='請選擇',
			actions=[
				MessageTemplateAction(
					label='北部地區天氣資訊',
					text='北部地區天氣資訊',
				),
				MessageTemplateAction(
					label='北部氣溫',
					text='北部氣溫',
				),
				MessageTemplateAction(
					label='北部降雨機率',
					text='北部降雨機率',
				)
			]
		)
	)
	message22=TemplateSendMessage(
		alt_text = '北部地區天氣資訊',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='基隆市',
					text='基隆市',
					actions=[
						URITemplateAction(
							label='基隆市資訊',
							uri='https://drive.google.com/file/d/1MMSm6Biv83WExOeQ-igryNhqOOfyoScq/view?usp=sharing'+profile.display_name+'&information=基隆市'
						)
					]
				),
				CarouselColumn(
					title='台北市',
					text='台北市',
					actions=[
						URITemplateAction(
							label='台北市資訊',
							uri='https://drive.google.com/file/d/1babio54C-4po1_OT6zNSaU8QLaw6rBBV/view?usp=sharing'+profile.display_name+'&information=台北市'
						)
					]
				),
				CarouselColumn(
					title='新北市',
					text='新北市',
					actions=[
						URITemplateAction(
							label='新北市資訊',
							uri='https://drive.google.com/file/d/1OtOcc0HIji5tUVeKJwXEvkUwJJvaOD7_/view?usp=sharing'+profile.display_name+'&information=新北市'
						)
					]
				),
				CarouselColumn(
					title='桃園市',
					text='桃園市',
					actions=[
						URITemplateAction(
							label='桃園市資訊',
							uri='https://drive.google.com/file/d/1KuKqxT-05cMbWf_uMm0RH6D17GEWuzXu/view?usp=sharing'+profile.display_name+'&information=桃園市'
						)
					]
				),
				CarouselColumn(
					title='新竹市',
					text='新竹市',
					actions=[
						URITemplateAction(
							label='新竹市資訊',
							uri='https://drive.google.com/file/d/1p3_xcDB1GibhPvVwhxj-VHUAPM-9U2te/view?usp=sharing'+profile.display_name+'&information=新竹市'
						)
					]
				),
				CarouselColumn(
					title='新竹縣',
					text='新竹縣',
					actions=[
						URITemplateAction(
							label='新竹縣資訊',
							uri='https://drive.google.com/file/d/1YZxqoO0IwQ6KBNKeBVjjHUl0RKpoa6Np/view?usp=sharing'+profile.display_name+'&information=新竹縣'
						)
					]
				),
				CarouselColumn(
					title='宜蘭縣',
					text='宜蘭縣',
					actions=[
						URITemplateAction(
							label='宜蘭縣資訊',
							uri='https://drive.google.com/file/d/1BbwfIkj7KJAfuo0R-vbEmvI8NWMpS0sZ/view?usp=sharing'+profile.display_name+'&information=宜蘭縣'
						)
					]
				)
			]
		)
	)
	message23=TemplateSendMessage(
		alt_text = '北部氣溫',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='基隆市',
					text='基隆市',
					actions=[
						URITemplateAction(
							label='基隆市氣溫',
							uri='https://drive.google.com/file/d/1klBzwH5DjIOfl-i4ype_9aoYrPvIKhq9/view?usp=sharing'+profile.display_name+'&information=基隆市'
						)
					]
				),
				CarouselColumn(
					title='台北市',
					text='台北市',
					actions=[
						URITemplateAction(
							label='台北市氣溫',
							uri='https://drive.google.com/file/d/1-F3myE8kQn_Vx24tWO_v9_KYaGXwmyAr/view?usp=sharing'+profile.display_name+'&information=台北市'
						)
					]
				),
				CarouselColumn(
					title='新北市',
					text='新北市',
					actions=[
						URITemplateAction(
							label='新北市氣溫',
							uri='https://drive.google.com/file/d/1swAw3t79Xjrff_ZtFu0-43HGX_AuxW31/view?usp=sharing'+profile.display_name+'&information=新北市'
						)
					]
				),
				CarouselColumn(
					title='桃園市',
					text='桃園市',
					actions=[
						URITemplateAction(
							label='桃園市氣溫',
							uri='https://drive.google.com/file/d/1pECn7-qWFh0Opo5D2U32EVz9nvP1e8ga/view?usp=sharing'+profile.display_name+'&information=桃園市'
						)
					]
				),
				CarouselColumn(
					title='新竹市',
					text='新竹市',
					actions=[
						URITemplateAction(
							label='新竹市氣溫',
							uri='https://drive.google.com/file/d/1b2g2yK4W0HzlcfFEGuPD1GfnRaIGGp_n/view?usp=sharing'+profile.display_name+'&information=新竹市'
						)
					]
				),
				CarouselColumn(
					title='新竹縣',
					text='新竹縣',
					actions=[
						URITemplateAction(
							label='新竹縣氣溫',
							uri='https://drive.google.com/file/d/1L2RzGcD2Dbt25gByklgAn-aEF3CLPXUk/view?usp=sharing'+profile.display_name+'&information=新竹縣'
						)
					]
				),
				CarouselColumn(
					title='宜蘭縣',
					text='宜蘭縣',
					actions=[
						URITemplateAction(
							label='宜蘭縣氣溫',
							uri='https://drive.google.com/file/d/1Q8XbBOSqxuqy46AtqmDhH50qM1eDOxXC/view?usp=sharing'+profile.display_name+'&information=宜蘭縣'
						)
					]
				)
			]
		)
	)
	message24=TemplateSendMessage(
		alt_text = '北部降雨機率',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='基隆市',
					text='基隆市',
					actions=[
						URITemplateAction(
							label='基隆市降雨機率',
							uri='https://drive.google.com/file/d/1Q_JmOD-kFu0SU0_50GUBCQ6aaIkDL2fH/view?usp=sharing'+profile.display_name+'&information=基隆市'
						)
					]
				),
				CarouselColumn(
					title='台北市',
					text='台北市',
					actions=[
						URITemplateAction(
							label='台北市降雨機率',
							uri='https://drive.google.com/file/d/14-5qWp5xUKP6dOryrDPvD_dhXSWTv5qc/view?usp=sharing'+profile.display_name+'&information=台北市'
						)
					]
				),
				CarouselColumn(
					title='新北市',
					text='新北市',
					actions=[
						URITemplateAction(
							label='新北市降雨機率',
							uri='https://drive.google.com/file/d/1_FTUrbQM9TmqL7zRnqnkiklNbaTl8JI-/view?usp=sharing'+profile.display_name+'&information=新北市'
						)
					]
				),
				CarouselColumn(
					title='桃園市',
					text='桃園市',
					actions=[
						URITemplateAction(
							label='桃園市降雨機率',
							uri='https://drive.google.com/file/d/1jOGmB-mqTUhquBK1JqB1MSHSglamTRLS/view?usp=sharing'+profile.display_name+'&information=桃園市'
						)
					]
				),
				CarouselColumn(
					title='新竹市',
					text='新竹市',
					actions=[
						URITemplateAction(
							label='新竹市降雨機率',
							uri='https://drive.google.com/file/d/1iuM6f_JUWBFS0FVafJMZM-Ua10BNWqTk/view?usp=sharing'+profile.display_name+'&information=新竹市'
						)
					]
				),
				CarouselColumn(
					title='新竹縣',
					text='新竹縣',
					actions=[
						URITemplateAction(
							label='新竹縣降雨機率',
							uri='https://drive.google.com/file/d/1-62jpDJhOueoJkyYtx3VClLLb2vUXQf7/view?usp=sharing'+profile.display_name+'&information=新竹縣'
						)
					]
				),
				CarouselColumn(
					title='宜蘭縣',
					text='宜蘭縣',
					actions=[
						URITemplateAction(
							label='宜蘭縣降雨機率',
							uri='https://drive.google.com/file/d/16ZyUtpCQqbQtJhVBtGtZWjkp-Se4a0DV/view?usp=sharing'+profile.display_name+'&information=宜蘭縣'
						)
					]
				)
			]
		)
	)
	message13 = TemplateSendMessage(
		alt_text = '中台灣',
		template=ButtonsTemplate(
			title='請選擇想要資訊',
			text='請選擇',
			actions=[
				MessageTemplateAction(
					label='中部地區天氣資訊',
					text='中部地區天氣資訊',
				),
				MessageTemplateAction(
					label='中部氣溫',
					text='中部氣溫',
				),
				MessageTemplateAction(
					label='中部降雨機率',
					text='中部降雨機率',
				)
			]
		)
	)
	message32=TemplateSendMessage(
		alt_text = '中部地區天氣資訊',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='苗栗縣',
					text='苗栗縣',
					actions=[
						URITemplateAction(
							label='苗栗縣資訊',
							uri='https://drive.google.com/file/d/1zcK3k84eh1R8hWgGik1djqIYlTEjswLY/view?usp=sharing'+profile.display_name+'&information=苗栗縣'
						)
					]
				),
				CarouselColumn(
					title='台中市',
					text='台中市',
					actions=[
						URITemplateAction(
							label='台中市資訊',
							uri='https://drive.google.com/file/d/12JUBeSN36e_4_WqmhkM5EE2--mRg75Av/view?usp=sharing'+profile.display_name+'&information=台中市'
						)
					]
				),
				CarouselColumn(
					title='彰化縣',
					text='彰化縣',
					actions=[
						URITemplateAction(
							label='彰化縣資訊',
							uri='https://drive.google.com/file/d/1lyMw03EjJwqFvgC2BJCjijZGeFpsRSQV/view?usp=sharing'+profile.display_name+'&information=彰化縣'
						)
					]
				),
				CarouselColumn(
					title='南投縣',
					text='南投縣',
					actions=[
						URITemplateAction(
							label='南投縣資訊',
							uri='https://drive.google.com/file/d/1FDm2QbKHSulbyJgGyACO_QvYQboTEA6V/view?usp=sharing'+profile.display_name+'&information=南投縣'
						)
					]
				),
				CarouselColumn(
					title='雲林縣',
					text='雲林縣',
					actions=[
						URITemplateAction(
							label='雲林縣資訊',
							uri='https://drive.google.com/file/d/1DkFxWMrWUVqPYm7vhrR7BN0NX15yXF4Z/view?usp=sharing'+profile.display_name+'&information=雲林縣'
						)
					]
				)
			]
		)
	)
	message33=TemplateSendMessage(
		alt_text = '中部氣溫',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='苗栗縣',
					text='苗栗縣',
					actions=[
						URITemplateAction(
							label='苗栗縣氣溫',
							uri='https://drive.google.com/file/d/1pH6-AtKmG09CXfLRcre41Tp4HnZT30Gl/view?usp=sharing'+profile.display_name+'&information=苗栗縣'
						)
					]
				),
				CarouselColumn(
					title='台中市',
					text='台中市',
					actions=[
						URITemplateAction(
							label='台中市氣溫',
							uri='https://drive.google.com/file/d/1V-5V01TkK-G5D5P2oL0TnpMZpnakjxrD/view?usp=sharing'+profile.display_name+'&information=台中市'
						)
					]
				),
				CarouselColumn(
					title='彰化縣',
					text='彰化縣',
					actions=[
						URITemplateAction(
							label='彰化縣氣溫',
							uri='https://drive.google.com/file/d/1CS5PNNFnmp2lhJti4MHE5nN4tLELoozV/view?usp=sharing'+profile.display_name+'&information=彰化縣'
						)
					]
				),
				CarouselColumn(
					title='南投縣',
					text='南投縣',
					actions=[
						URITemplateAction(
							label='南投縣氣溫',
							uri='https://drive.google.com/file/d/1G9kysIftAh67MyXJOQMVqdn03OEUpLFe/view?usp=sharing'+profile.display_name+'&information=南投縣'
						)
					]
				),
				CarouselColumn(
					title='雲林縣',
					text='雲林縣',
					actions=[
						URITemplateAction(
							label='雲林縣氣溫',
							uri='https://drive.google.com/file/d/1Tu5RsFCSGpwxrMnI1Y4beamcx65yP9MT/view?usp=sharing'+profile.display_name+'&information=雲林縣'
						)
					]
				)
			]
		)
	)
	message32=TemplateSendMessage(
		alt_text = '中部降雨機率',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='苗栗縣',
					text='苗栗縣',
					actions=[
						URITemplateAction(
							label='苗栗縣降雨機率',
							uri='https://drive.google.com/file/d/1KJZN2DTSx0zb-E2LWHrmvVtK6IoH7A2x/view?usp=sharing'+profile.display_name+'&information=苗栗縣'
						)
					]
				),
				CarouselColumn(
					title='台中市',
					text='台中市',
					actions=[
						URITemplateAction(
							label='台中市降雨機率',
							uri='https://drive.google.com/file/d/1vITVqfYQYPwlZFMoULS3ZaQGlE9CrUEj/view?usp=sharing'+profile.display_name+'&information=台中市'
						)
					]
				),
				CarouselColumn(
					title='彰化縣',
					text='彰化縣',
					actions=[
						URITemplateAction(
							label='彰化縣降雨機率',
							uri='https://drive.google.com/file/d/1kyw2s40Kw75hV_19tQJ7G1UX0t6z8sEs/view?usp=sharing'+profile.display_name+'&information=彰化縣'
						)
					]
				),
				CarouselColumn(
					title='南投縣',
					text='南投縣',
					actions=[
						URITemplateAction(
							label='南投縣降雨機率',
							uri='https://drive.google.com/file/d/1us52IrZSonVNjPJlRNGawkKcX14cgHFG/view?usp=sharing'+profile.display_name+'&information=南投縣'
						)
					]
				),
				CarouselColumn(
					title='雲林縣',
					text='雲林縣',
					actions=[
						URITemplateAction(
							label='雲林縣降雨機率',
							uri='https://drive.google.com/file/d/1RLrmU6n1UIsjmVdooKD8LIH8P7SilFiX/view?usp=sharing'+profile.display_name+'&information=雲林縣'
						)
					]
				)
			]
		)
	)
	message14 = TemplateSendMessage(
		alt_text = '南台灣',
		template=ButtonsTemplate(
			title='請選擇想要資訊',
			text='請選擇',
			actions=[
				MessageTemplateAction(
					label='南部地區天氣資訊',
					text='南部地區天氣資訊',
				),
				MessageTemplateAction(
					label='南部氣溫',
					text='南部氣溫',
				),
				MessageTemplateAction(
					label='南部降雨機率',
					text='南部降雨機率',
				)
			]
		)
	)
	message42=TemplateSendMessage(
		alt_text = '南部地區天氣資訊',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='嘉義縣',
					text='嘉義縣',
					actions=[
						URITemplateAction(
							label='嘉義縣資訊',
							uri='https://drive.google.com/file/d/1ypeneYINdf1_eoIkxiBukQUQLAMctNcI/view?usp=sharing'+profile.display_name+'&information=嘉義縣'
						)
					]
				),
				CarouselColumn(
					title='嘉義市',
					text='嘉義市',
					actions=[
						URITemplateAction(
							label='嘉義市資訊',
							uri='https://drive.google.com/file/d/1Q8PfK42HQdJpZXQs613za4Eztbyfuyny/view?usp=sharing'+profile.display_name+'&information=嘉義市'
						)
					]
				),
				CarouselColumn(
					title='台南市',
					text='台南市',
					actions=[
						URITemplateAction(
							label='台南市資訊',
							uri='https://drive.google.com/file/d/1t9VmBQR4vHPq72Uuj4Nutp2s2wI3F971/view?usp=sharing'+profile.display_name+'&information=台南市'
						)
					]
				),
				CarouselColumn(
					title='高雄市',
					text='高雄市',
					actions=[
						URITemplateAction(
							label='高雄市資訊',
							uri='https://drive.google.com/file/d/1IBEWBe56cNU24I3SOI7OEhD54K-hD5Ar/view?usp=sharing'+profile.display_name+'&information=高雄市'
						)
					]
				),
				CarouselColumn(
					title='屏東縣',
					text='屏東縣',
					actions=[
						URITemplateAction(
							label='屏東縣資訊',
							uri='https://drive.google.com/file/d/1KnsTG5RmUrDGt9q4tIExjhN4jeV2xCQ4/view?usp=sharing'+profile.display_name+'&information=屏東縣'
						)
					]
				)
			]
		)
	)
	message43=TemplateSendMessage(
		alt_text = '南部氣溫',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='嘉義縣',
					text='嘉義縣',
					actions=[
						URITemplateAction(
							label='嘉義縣氣溫',
							uri='https://drive.google.com/file/d/1VRmzXk4m8UXgmjzM0Cjqm2QPKJoScvaM/view?usp=sharing'+profile.display_name+'&information=嘉義縣'
						)
					]
				),
				CarouselColumn(
					title='嘉義市',
					text='嘉義市',
					actions=[
						URITemplateAction(
							label='嘉義市氣溫',
							uri='https://drive.google.com/file/d/1pSQmBc3UPv_BYHdDL6iySiJlXwUKlcnn/view?usp=sharing'+profile.display_name+'&information=嘉義市'
						)
					]
				),
				CarouselColumn(
					title='台南市',
					text='台南市',
					actions=[
						URITemplateAction(
							label='台南市氣溫',
							uri='https://drive.google.com/file/d/1ZVVIifzjJKDmkrbXSgyhWVOPYCZVgVDJ/view?usp=sharing'+profile.display_name+'&information=台南市'
						)
					]
				),
				CarouselColumn(
					title='高雄市',
					text='高雄市',
					actions=[
						URITemplateAction(
							label='高雄市氣溫',
							uri='https://drive.google.com/file/d/1-t25ZuHka6K2cJvNxKnJOFiE47QoTo1R/view?usp=sharing'+profile.display_name+'&information=高雄市'
						)
					]
				),
				CarouselColumn(
					title='屏東縣',
					text='屏東縣',
					actions=[
						URITemplateAction(
							label='屏東縣氣溫',
							uri='https://drive.google.com/file/d/1El2YlPpuTLRA_31N8RfxRWhgT3trBfxY/view?usp=sharing'+profile.display_name+'&information=屏東縣'
						)
					]
				)
			]
		)
	)
	message44=TemplateSendMessage(
		alt_text = '南部降雨機率',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='嘉義縣',
					text='嘉義縣',
					actions=[
						URITemplateAction(
							label='嘉義縣降雨機率',
							uri='https://drive.google.com/file/d/1HiBgNUK7XF8DtI4HzQKfvBP-5VKhHVi7/view?usp=sharing'+profile.display_name+'&information=嘉義縣'
						)
					]
				),
				CarouselColumn(
					title='嘉義市',
					text='嘉義市',
					actions=[
						URITemplateAction(
							label='嘉義市降雨機率',
							uri='https://drive.google.com/file/d/13FDby9fpb81xsngke2GZxj8eTUKNiva2/view?usp=sharing'+profile.display_name+'&information=嘉義市'
						)
					]
				),
				CarouselColumn(
					title='台南市',
					text='台南市',
					actions=[
						URITemplateAction(
							label='台南市降雨機率',
							uri='https://drive.google.com/file/d/1fU_mkuN_8dNo-29rFXLh9d88-Kq19mmQ/view?usp=sharing'+profile.display_name+'&information=台南市'
						)
					]
				),
				CarouselColumn(
					title='高雄市',
					text='高雄市',
					actions=[
						URITemplateAction(
							label='高雄市降雨機率',
							uri='https://drive.google.com/file/d/1ISH6xXduwZi7FobBT-x5sVcz4FqP0hNZ/view?usp=sharing'+profile.display_name+'&information=高雄市'
						)
					]
				),
				CarouselColumn(
					title='屏東縣',
					text='屏東縣',
					actions=[
						URITemplateAction(
							label='屏東縣降雨機率',
							uri='https://drive.google.com/file/d/1K4f_SS9-8zPX2wIU7F5BO07OuGwsIYvd/view?usp=sharing'+profile.display_name+'&information=屏東縣'
						)
					]
				)
			]
		)
	)
	message15 = TemplateSendMessage(
		alt_text = '東台灣',
		template=ButtonsTemplate(
			title='請選擇想要資訊',
			text='請選擇',
			actions=[
				MessageTemplateAction(
					label='東部地區天氣資訊',
					text='東部地區天氣資訊',
				),
				MessageTemplateAction(
					label='東部氣溫',
					text='東部氣溫',
				),
				MessageTemplateAction(
					label='東部降雨機率',
					text='東部降雨機率',
				)
			]
		)
	)
	message52=TemplateSendMessage(
		alt_text = '東部地區天氣資訊',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='花蓮縣',
					text='花蓮縣',
					actions=[
						URITemplateAction(
							label='花蓮縣資訊',
							uri='https://drive.google.com/file/d/1vtqh5WY1kj8S1FS9hiPFlpOhYRoq_ZSJ/view?usp=sharing'+profile.display_name+'&information=花蓮縣'
						)
					]
				),
				CarouselColumn(
					title='台東縣',
					text='台東縣',
					actions=[
						URITemplateAction(
							label='台東縣資訊',
							uri='https://drive.google.com/file/d/1eiJuxFDkMV_I1YvMWYVrZCyylrG1YPhM/view?usp=sharing'+profile.display_name+'&information=台東縣'
						)
					]
				)
			]
		)
	)
	message53=TemplateSendMessage(
		alt_text = '東部氣溫',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='花蓮縣',
					text='花蓮縣',
					actions=[
						URITemplateAction(
							label='花蓮縣氣溫',
							uri='https://drive.google.com/file/d/1fFc9OyxUkYh8Ynf_yt8Hx0YOcu7fADn1/view?usp=sharing'+profile.display_name+'&information=花蓮縣'
						)
					]
				),
				CarouselColumn(
					title='台東縣',
					text='台東縣',
					actions=[
						URITemplateAction(
							label='台東縣氣溫',
							uri='https://drive.google.com/file/d/1QlkC8JaudiPv8XtP3CbcLguJa4DUuoM4/view?usp=sharing'+profile.display_name+'&information=台東縣'
						)
					]
				)
			]
		)
	)
	message54=TemplateSendMessage(
		alt_text = '東部降雨機率',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='花蓮縣',
					text='花蓮縣',
					actions=[
						URITemplateAction(
							label='花蓮縣降雨機率',
							uri='https://drive.google.com/file/d/1ZSRGOiGdCXc5MovOZqrTRROqNUiGGqmu/view?usp=sharing'+profile.display_name+'&information=花蓮縣'
						)
					]
				),
				CarouselColumn(
					title='台東縣',
					text='台東縣',
					actions=[
						URITemplateAction(
							label='台東縣降雨機率',
							uri='https://drive.google.com/file/d/17XoN3rQehVhmtwmiflUOCiB6kOb0Q8NU/view?usp=sharing'+profile.display_name+'&information=台東縣'
						)
					]
				)
			]
		)
	)
	message16 = TemplateSendMessage(
		alt_text = '離島',
		template=ButtonsTemplate(
			title='請選擇想要資訊',
			text='請選擇',
			actions=[
				MessageTemplateAction(
					label='離島地區天氣資訊',
					text='離島地區天氣資訊',
				),
				MessageTemplateAction(
					label='離島氣溫',
					text='離島氣溫',
				),
				MessageTemplateAction(
					label='離島降雨機率',
					text='離島降雨機率',
				)
			]
		)
	)
	message62=TemplateSendMessage(
		alt_text = '離島地區天氣資訊',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='澎湖縣',
					text='澎湖縣',
					actions=[
						URITemplateAction(
							label='澎湖縣資訊',
							uri='https://drive.google.com/file/d/13QQT36cajwepniQfu9r2kmbzGyD6P36Z/view?usp=sharing'+profile.display_name+'&information=澎湖縣'
						)
					]
				),
				CarouselColumn(
					title='金門縣',
					text='金門縣',
					actions=[
						URITemplateAction(
							label='金門縣資訊',
							uri='https://drive.google.com/file/d/1u_GPsp1Fx5zJMRcWvQr86vGcAogKwKQU/view?usp=sharing'+profile.display_name+'&information=金門縣'
						)
					]
				),
				CarouselColumn(
					title='連江縣',
					text='連江縣',
					actions=[
						URITemplateAction(
							label='連江縣資訊',
							uri='https://drive.google.com/file/d/1kBbKPTogMS7hptmQ6Hzk7iYYHFJXc53t/view?usp=sharing'+profile.display_name+'&information=連江縣'
						)
					]
				)
			]
		)
	)
	message63=TemplateSendMessage(
		alt_text = '離島氣溫',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='澎湖縣',
					text='澎湖縣',
					actions=[
						URITemplateAction(
							label='澎湖縣氣溫',
							uri='https://drive.google.com/file/d/1Jz8XwizzSHRbCxhoGzigdDtrlZ1QWFIx/view?usp=sharing'+profile.display_name+'&information=澎湖縣'
						)
					]
				),
				CarouselColumn(
					title='金門縣',
					text='金門縣',
					actions=[
						URITemplateAction(
							label='金門縣氣溫',
							uri='https://drive.google.com/file/d/1dF4kx0NU9LAoiExAc-iEAHkhWEPprTmw/view?usp=sharing'+profile.display_name+'&information=金門縣'
						)
					]
				),
				CarouselColumn(
					title='連江縣',
					text='連江縣',
					actions=[
						URITemplateAction(
							label='連江縣氣溫',
							uri='https://drive.google.com/file/d/1c4eC_SCLcCz0eTf7SjQOffPl-jlIq9uI/view?usp=sharing'+profile.display_name+'&information=連江縣'
						)
					]
				)
			]
		)
	)
	message64=TemplateSendMessage(
		alt_text = '離島降雨機率',
		template=CarouselTemplate(
			columns=[
				CarouselColumn(
					title='澎湖縣',
					text='澎湖縣',
					actions=[
						URITemplateAction(
							label='澎湖縣降雨機率',
							uri='https://drive.google.com/file/d/1BVWCrGBahPnJ89xTggE12vvWNs7MRSDm/view?usp=sharing'+profile.display_name+'&information=澎湖縣'
						)
					]
				),
				CarouselColumn(
					title='金門縣',
					text='金門縣',
					actions=[
						URITemplateAction(
							label='金門縣降雨機率',
							uri='https://drive.google.com/file/d/1J4NL3rm3cJQl3xd9qpwLLcmxG1uh0D3o/view?usp=sharing'+profile.display_name+'&information=金門縣'
						)
					]
				),
				CarouselColumn(
					title='連江縣',
					text='連江縣',
					actions=[
						URITemplateAction(
							label='連江縣降雨機率',
							uri='https://drive.google.com/file/d/19ixayzYvcQtPxMgMFIHd1zfKEapCddKe/view?usp=sharing'+profile.display_name+'&information=連江縣'
						)
					]
				)
			]
		)
	)
	if event.message.text == "天氣資訊":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message)
	elif event.message.text == "桃園市":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message1)
	elif event.message.text == "完整天氣資訊":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, [message2,message3])
	elif event.message.text == "氣溫":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, [message4,message5])
	elif event.message.text == "降雨機率":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, [message6,message7])
	elif event.message.text == "台灣":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message11)
	elif event.message.text == "北台灣":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message12)
	elif event.message.text == "中台灣":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message13)
	elif event.message.text == "南台灣":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message14)
	elif event.message.text == "東台灣":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message15)
	elif event.message.text == "離島":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message16)
	elif event.message.text == "北部地區天氣資訊":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message22)
	elif event.message.text == "北部氣溫":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message23)
	elif event.message.text == "北部降雨機率":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message24)
	
	elif event.message.text == "中部地區天氣資訊":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message32)
	elif event.message.text == "中部氣溫":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message33)
	elif event.message.text == "中部降雨機率":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message34)
		
	elif event.message.text == "南部地區天氣資訊":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message42)
	elif event.message.text == "南部氣溫":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message43)
	elif event.message.text == "南部降雨機率":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message44)
		
	elif event.message.text == "東部地區天氣資訊":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message52)
	elif event.message.text == "東部氣溫":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message53)
	elif event.message.text == "東部降雨機率":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message54)
		
	elif event.message.text == "離島地區天氣資訊":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message62)
	elif event.message.text == "離島氣溫":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message63)
	elif event.message.text == "離島降雨機率":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message64)
	else:
		line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
	app.run()
