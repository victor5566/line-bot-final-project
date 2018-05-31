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
app = Flask(__name__)

line_bot_api = LineBotApi('biJ0HeVMeHTfUlDNl3Y+9PkPZLS29zFw1NEjByQFvmfMgN2MPGSSzRZ2AsGLKypbFhCccneoY66OmUJGPWtW8aYj8AY2Rkq7oDy8Wuasi1rLVhc2HHG+cPbEJ/rmPA7SOuuaUs6J0KtQXS+d2+CAswdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('99dc133cdb2d254f5b37aa0d86fc1980')
message = TemplateSendMessage(
	alt_text = '天氣資訊',
	template=ButtonsTemplate(
		title='請選擇城市',
		text='請選擇',
		actions=[
			MessageTemplateAction(
				label='桃園市',
				text='桃園市',
			),
			MessageTemplateAction(
				label='氣溫',
				text='氣溫',
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
	message2=TemplateSendMessage(
		alt_text = '桃園市',
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
		alt_text = '桃園市',
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
	
	if event.message.text == "天氣資訊":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, message)
	elif event.message.text == "桃園市":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, [message2,message3])
	elif event.message.text == "氣溫":
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(event.reply_token, [message4,message5])
	else:
		line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
	app.run()
