import random
import ftplib

def main():
    ip = ".".join(map(str, (random.randint(0, 255)
                                      for _ in range(4))))

    def anonLogin(hostname):
        print(ip)
        try:
            ftp = ftplib.FTP(hostname, timeout=9)
            ftp.login('anonymous')
            print('\n [+]' + str(hostname) + ' FTP Anonymous Login Succeded.')
            ftp.quit()
            return True
        except Exception:
            print('\n [-] ' + str(hostname) + ' FTP Anonymous Login Fails.')
            print('Next IP...')
            main()
    if __name__ == '__main__':
        anonLogin(ip)
main()
