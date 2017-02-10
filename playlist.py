import random

SOURCES = [
    "http://watchcartoonsonline.eu/get_video.php?token=7k7X7Vek7S7S7_eY7O7C7Oe47U7z7z7s7r7.747-7g777q7F7A7t7G7b777e7m7.7h707P7x7jed7R7U7R7eer7j7P7Tef707~7s7q7Qed7e72er7e7z7_7T7P7~7~737A7Udaaf9825006580d7b70f772b02f977c9fd231c2745ac534613b455570228d070jVjNjcNLjzNJNs7wND7djGNoNqN1jhNujmjKjojbN~7aNyj.jeNmN1jENyNONhjq72jVNnNf7fNtjTjgNYNCNmNqjgN7N8NYjNNZjpjp7RNGNvNx72NljxNTNgNajpN4NiN_NyNlN-N3j3N6NRNGNrNgNWNEjbjMNtNAjiNsjKNyN27YN_NuNDjCNXNV7yNKNujeN0N8NgNw7HNtNWjnjmNbNDNvN8Nm7fjTj5jjNlNJNTNXN07oN.jbjgNKNljAjzj7N0jLjjNLNR7Zj6jpN3NLj37ujVNcNHjMNxN4N.NPjCNRNxNYNkj.N.jcNEN.7lNO7ZNq"
    # "https://r4---sn-gpv7enek.googlevideo.com/videoplayback?id=3c66abd70d824eca&itag=18&source=picasa&begin=0&requiressl=yes&mm=30&mn=sn-gpv7enek&ms=nxu&mv=m&nh=IgpwcjAzLnJpbzAxKhgyMDAxOjQ4NjA6MToxOjA6MWUzYTowOjE&pl=36&sc=yes&mime=video/mp4&lmt=1443168749462780&mt=1485398536&ip=2804:d41:18d8:5500:b4fb:4845:83cd:ebc4&ipbits=48&expire=1485427401&sparams=ip,ipbits,expire,id,itag,source,requiressl,mm,mn,ms,mv,nh,pl,sc,mime,lmt&signature=B07FF5785B133107FB925EED180ED04CFF8F5537.51062A367DE9F7E05703E1847330132CA81F8990&key=ck2",
    # "https://r2---sn-gpv7enek.googlevideo.com/videoplayback?id=97df02b994678ec3&itag=18&source=picasa&begin=0&requiressl=yes&mm=30&mn=sn-gpv7enek&ms=nxu&mv=m&nh=IgpwcjAzLnJpbzAxKhkyMDAxOjQ4NjA6MToxOjA6MWUzYTowOjE3&pl=36&sc=yes&mime=video/mp4&lmt=1443169235439184&mt=1485400158&ip=2804:d41:18d8:5500:b4fb:4845:83cd:ebc4&ipbits=48&expire=1485429046&sparams=ip,ipbits,expire,id,itag,source,requiressl,mm,mn,ms,mv,nh,pl,sc,mime,lmt&signature=67F9D7445CE58B86BE3678226906FD7317820539.933F269F466246A210381CDCFC10C4CE5ABAC198&key=ck2",
    # "https://r5---sn-gpv7eney.googlevideo.com/videoplayback?id=14a19e864019af0f&itag=18&source=picasa&begin=0&requiressl=yes&mm=30&mn=sn-gpv7eney&ms=nxu&mv=m&nh=IgpwcjAzLnJpbzAxKhkyMDAxOjQ4NjA6MToxOjA6MWUzYTowOjE3&pl=36&sc=yes&mime=video/mp4&lmt=1443166750593694&mt=1485400339&ip=2804:d41:18d8:5500:b4fb:4845:83cd:ebc4&ipbits=48&expire=1485429250&sparams=ip,ipbits,expire,id,itag,source,requiressl,mm,mn,ms,mv,nh,pl,sc,mime,lmt&signature=19CD5AC88469B1E5B6FD079AB208DB46AE4BC4D3.B6A051AD02294A997F90CAF3D3831DE30A372644&key=ck2",
    # "https://r4---sn-gpv7eney.googlevideo.com/videoplayback?id=fdda707331dec7ac&itag=18&source=picasa&begin=0&requiressl=yes&mm=30&mn=sn-gpv7eney&ms=nxu&mv=m&nh=IgpwcjAzLnJpbzAxKhgyMDAxOjQ4NjA6MToxOjA6MWUzYTowOmI&pl=36&sc=yes&mime=video/mp4&lmt=1443167694927212&mt=1485400339&ip=2804:d41:18d8:5500:b4fb:4845:83cd:ebc4&ipbits=48&expire=1485429289&sparams=ip,ipbits,expire,id,itag,source,requiressl,mm,mn,ms,mv,nh,pl,sc,mime,lmt&signature=4D6C36A2EC93CE649D5FEA40B85ADE551EBE0A43.8E8DE4CFB66E1B359C25095864FF47D11CA53CD8&key=ck2",
    # "https://r4---sn-gpv7eney.googlevideo.com/videoplayback?id=83a74834284f973d&itag=18&source=picasa&begin=0&requiressl=yes&mm=30&mn=sn-gpv7eney&ms=nxu&mv=m&nh=IgpwcjAzLnJpbzAxKhkyMDAxOjQ4NjA6MToxOjA6MWUzYTowOjEx&pl=36&sc=yes&mime=video/mp4&lmt=1443167855798288&mt=1485400518&ip=2804:d41:18d8:5500:b4fb:4845:83cd:ebc4&ipbits=48&expire=1485429403&sparams=ip,ipbits,expire,id,itag,source,requiressl,mm,mn,ms,mv,nh,pl,sc,mime,lmt&signature=B8B729842D3CB2CA60E6A9510526874F419D79F0.36B7F2DBA0AF8BA71FD10266B9A50DDA0C1AF4AB&key=ck2",
    # "https://r6---sn-gpv7ener.googlevideo.com/videoplayback?id=32e9a980deafc354&itag=18&source=picasa&begin=0&requiressl=yes&mm=30&mn=sn-gpv7ener&ms=nxu&mv=m&nh=IgpwcjAzLnJpbzAxKhkyMDAxOjQ4NjA6MToxOjA6MWUzYTowOjFi&pl=36&sc=yes&mime=video/mp4&lmt=1443168793772620&mt=1485400518&ip=2804:d41:18d8:5500:b4fb:4845:83cd:ebc4&ipbits=48&expire=1485429447&sparams=ip,ipbits,expire,id,itag,source,requiressl,mm,mn,ms,mv,nh,pl,sc,mime,lmt&signature=9531BC031F8032C09E645ABDC5BAA6E54A59403A.1C02B3538DC4F2D670B8F75316889DB1110DE60C&key=ck2",
    # "https://r2---sn-gpv7ener.googlevideo.com/videoplayback?id=9bae457b327a736d&itag=18&source=picasa&begin=0&requiressl=yes&mm=30&mn=sn-gpv7ener&ms=nxu&mv=m&nh=IgpwcjAzLnJpbzAxKhkyMDAxOjQ4NjA6MToxOjA6MWUzYTowOjI3&pl=36&sc=yes&mime=video/mp4&lmt=1443165964711621&mt=1485400518&ip=2804:d41:18d8:5500:b4fb:4845:83cd:ebc4&ipbits=48&expire=1485429487&sparams=ip,ipbits,expire,id,itag,source,requiressl,mm,mn,ms,mv,nh,pl,sc,mime,lmt&signature=9668758953E6384AC51E04144DEF96D9127508CD.2F24B6518B0403E2F03489F21F60C72188286B2B&key=ck2",
]


def get_video_src():
    return random.choice(SOURCES)
