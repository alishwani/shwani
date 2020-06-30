import ftplib
def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'anonymous')
        print('\n[*] ' + str(hostname) + '\FTP anonymous Logon Succeeded.')
        
        ftp.quit()
        return True
    except Exception as e:
        print('\n[ - ] ' + str(hostname) + '\n FTP Anonymous Logon Failed.')
        
        return False
host ='IP Address'
anonLogin(host)
