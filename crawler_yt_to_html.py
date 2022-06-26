import urllib.request as req
import json

url="https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8"

#建立request物件 附加 headers  data資訊  
#requestData={"context":{"client":{"hl":"zh-TW","gl":"TW","remoteHost":"2001:b011:3817:1d0f:4573:e5d1:9902:1630","deviceMake":"","deviceModel":"","visitorData":"CgtxaV9NOFMwdFZtbyiQz8WQBg%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36,gzip(gfe)","clientName":"WEB","clientVersion":"2.20220217.07.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://www.youtube.com/","platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":{"appInstallData":"CJDPxZAGEJjqrQUQwvKtBRC3y60FEIfS_RIQkfj8EhDYvq0F"},"timeZone":"Asia/Taipei","browserName":"Chrome","browserVersion":"98.0.4758.102","screenWidthPoints":1491,"screenHeightPoints":1082,"screenPixelDensity":1,"screenDensityFloat":0.8333333730697632,"utcOffsetMinutes":480,"userInterfaceTheme":"USER_INTERFACE_THEME_LIGHT","memoryTotalKbytes":"8000000","mainAppWebInfo":{"graftUrl":"/","pwaInstallabilityStatus":"PWA_INSTALLABILITY_STATUS_UNKNOWN","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","isWebNativeShareAvailable":"true"}},"user":{"lockedSafetyMode":"false"},"request":{"useSsl":"true","consistencyTokenJars":[{"encryptedTokenJarContents":"AGDxDeNnCDqnGi3wFRGGZFI1GHeFEFU-KuKkJcqFwMElNdgfd9WAD9TVm8aqETFv8RoptmHFLQVJmycgoWrhywgF6G7H3aVJh9lw0P4d7XI8k9cIENY_lvM5YBSsmNEkqhbi9u6HMhDpY5T5Ok5IXA","expirationSeconds":"600"}],"internalExperimentFlags":[]},"clickTracking":{"clickTrackingParams":"CBgQsV4iEwiara-U4Yz2AhWJMVgKHfhPAZw="},"adSignalsInfo":{"params":[{"key":"dt","value":"1645307792451"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"480"},{"key":"u_his","value":"1"},{"key":"u_h","value":"864"},{"key":"u_w","value":"1536"},{"key":"u_ah","value":"824"},{"key":"u_aw","value":"1536"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"1082"},{"key":"biw","value":"1476"},{"key":"brdim","value":"0,0,0,0,1536,0,1536,824,1491,1082"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}]}},"browseId":"FEwhat_to_watch"}
requestData={"context":{"client":{"hl":"zh-TW","gl":"TW","remoteHost":"2001:b011:3817:1d0f:4573:e5d1:9902:1630","deviceMake":"","deviceModel":"","visitorData":"CgtxaV9NOFMwdFZtbyiQz8WQBg%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36,gzip(gfe)","clientName":"WEB","clientVersion":"2.20220217.07.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://www.youtube.com/","platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":{"appInstallData":"CJDPxZAGEJjqrQUQwvKtBRC3y60FEIfS_RIQkfj8EhDYvq0F"},"timeZone":"Asia/Taipei","browserName":"Chrome","browserVersion":"98.0.4758.102","screenWidthPoints":1491,"screenHeightPoints":1082,"screenPixelDensity":1,"screenDensityFloat":0.8333333730697632,"utcOffsetMinutes":480,"userInterfaceTheme":"USER_INTERFACE_THEME_LIGHT","memoryTotalKbytes":"8000000","mainAppWebInfo":{"graftUrl":"/","pwaInstallabilityStatus":"PWA_INSTALLABILITY_STATUS_UNKNOWN","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","isWebNativeShareAvailable":"true"}},"user":{"lockedSafetyMode":"false"},"request":{"useSsl":"true","consistencyTokenJars":[{"encryptedTokenJarContents":"AGDxDeNnCDqnGi3wFRGGZFI1GHeFEFU-KuKkJcqFwMElNdgfd9WAD9TVm8aqETFv8RoptmHFLQVJmycgoWrhywgF6G7H3aVJh9lw0P4d7XI8k9cIENY_lvM5YBSsmNEkqhbi9u6HMhDpY5T5Ok5IXA","expirationSeconds":"600"}],"internalExperimentFlags":[]},"clickTracking":{"clickTrackingParams":"CBgQsV4iEwiara-U4Yz2AhWJMVgKHfhPAZw="},"adSignalsInfo":{"params":[{"key":"dt","value":"1645307792451"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"480"},{"key":"u_his","value":"1"},{"key":"u_h","value":"864"},{"key":"u_w","value":"1536"},{"key":"u_ah","value":"824"},{"key":"u_aw","value":"1536"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"1082"},{"key":"biw","value":"1476"},{"key":"brdim","value":"0,0,0,0,1536,0,1536,824,1491,1082"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}]}},"browseId":"FEwhat_to_watch"}

request=req.Request(url ,headers={
    "content-type" : "application/json",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
},data=json.dumps(requestData).encode("utf-8"))
#發出請求
with req.urlopen(request) as response:
    result=response.read().decode("utf-8")
#print(result)
result=json.loads(result)
#印出一個文章標題
#print(result["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][1]["tabRenderer"]["content"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]["gridRenderer"]["items"])

items=result["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][0]["tabRenderer"]["content"]["richGridRenderer"]["contents"]

print("推薦你看1部片")
print("\n")

print(items[0]["richItemRenderer"]["content"]["videoRenderer"]["title"]["runs"][0]["text"])#名稱
print(items[0]["richItemRenderer"]["content"]["videoRenderer"]["viewCountText"]["simpleText"])#觀看數
print(items[0]["richItemRenderer"]["content"]["videoRenderer"]["lengthText"]["accessibility"]["accessibilityData"]["label"])#影片長度
print(items[0]["richItemRenderer"]["content"]["videoRenderer"]["publishedTimeText"]["simpleText"])#發布日期
print(items[0]["richItemRenderer"]["content"]["videoRenderer"]["ownerText"]["runs"][0]["text"])#頻道主人
print("https://www.youtube.com/watch?v="+items[0]["richItemRenderer"]["content"]["videoRenderer"]["videoId"])#影片連結
print("\n")
import os

#os.system("pause")
text="<title>隨機一部影片</title><h1>隨機一部影片-->"+items[0]["richItemRenderer"]["content"]["videoRenderer"]["title"]["runs"][0]["text"]+"</h1>"

html="""<iframe width="800" height="450" src="https://www.youtube.com/embed/"""
yturl=items[0]["richItemRenderer"]["content"]["videoRenderer"]["videoId"]
html2="""" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""

text2="<h4>"+items[0]["richItemRenderer"]["content"]["videoRenderer"]["viewCountText"]["simpleText"]+"</h4>"
text3="<h4>影片長度 : "+items[0]["richItemRenderer"]["content"]["videoRenderer"]["lengthText"]["accessibility"]["accessibilityData"]["label"]+"</h4>"
text4="<h4>發布日期 : "+items[0]["richItemRenderer"]["content"]["videoRenderer"]["publishedTimeText"]["simpleText"]+"</h4>"
text5="<h4>頻道主人 : "+items[0]["richItemRenderer"]["content"]["videoRenderer"]["ownerText"]["runs"][0]["text"]+"</h4>"
f = open("C:/Users/yeni1/Desktop/py_yt_to_html/result_to_youtube.html","w",encoding="utf-8")
f.write(text)
f.write(html)
f.write(yturl)
f.write(html2)
f.write(text2)
f.write(text3)
f.write(text4)
f.write(text5)
f.close()


