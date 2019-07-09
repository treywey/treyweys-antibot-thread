#Documentation with short script as help to bypass Sucuri Cloudproxy security, in this case on the site 'Footdistrict.com'

#starting with the script:
#the site will usually automaticallly redirect after a short browser check, but the check can obviously not be done in pure requests, so we need to 'solve' it
#check this first snippet and wait for the next explanations

mport requests
import js2py
import json
import ssl
import base64
import datetime
from bs4 import BeautifulSoup as bs

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "ECDH+AES128" #spoofing ciphers


#first, we need to get the sucuri script, let's get it from FootDistrict's website
print(str(datetime.datetime.now())+"< [INFO] Getting Site.")
req=requests.get("https://footdistrict.com/", headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"})
#lets soup the response text up lol 
try:
    print(str(datetime.datetime.now())+" < [INFO] Found SucuriProtection Script")
    script_unp=req.text.replace('''<html><title>You are being redirected...</titl^^
<noscript>Javascript is required. Please enable javascript before you are allowed to see this page.</noscript>
<script>''', '')
    print(str(datetime.datetime.now())+" < [INFO] Parsing Script")
    script_unp=script_unp.replace("</script></html>", "")
    split_scr_one=script_unp.split(",")[11]
    split_scr_two=split_scr_one.split(";")[0].replace("S='","")
    scr_enc=split_scr_two.replace("'", "")
    script_unpatched_decrypted=base64.b64decode(scr_enc)
    
    #until here we got the site, parsed the html and got the challenge script, we cleaned it and decoded a base64 string inside, after having a look at the now decoded part we see, there's actually another script inside
    #the script inside generates the cookies
    #now we have it and can simply patch it, by replacing the var document.cookie with cookie and by replacing location.reload() with console.log cookie
    #once we patched it, we have to run it with js2py, as simple as this
    f=js2py.eval_js(patched_script)
    f
    and we will get an output with our Sucuri Cookie, we can use it to access the site, pretty easy, isn't it? 
    #sucuri_cloudproxy_uuid_4537f229b':'f27f17b8903cd9fc8abcfad927315215'
    #PLEASE do  not think : 'haey i aM a gEnIuS i CoUlD jUsT use everytime the same one so i dont need to patch it, as each script is individual and creates different cookies. Using the same one more times will create the exactly same cookie tho (invalid then)

