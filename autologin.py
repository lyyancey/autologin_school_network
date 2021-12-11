from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging
import socket


class LoggerConf(object):
    def __init__(self, log_file_name):
        self.log_file_name = log_file_name

    def config(self):
        logger = logging.getLogger()
        fh = logging.FileHandler(self.log_file_name, encoding='utf-8', mode='a')
        formatter = logging.Formatter(
            '%(asctime)s - %(filename)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.setLevel(logging.INFO)


class Login(object):
    def __init__(self, userid, password, addr):
        self.userid = userid
        self.password = password
        self.address = addr
        self.driver = None

    def isNetOk(self, host="8.8.8.8", port=53, timeout=5):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error as ex:
            logging.info(ex)
            return False

    def auto_login(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.maximize_window()
        self.driver.get(self.address)

        # 等待页面加载
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html[1]/body[1]/app-root['
                                                                                         '1]/app-right-root[1]/div['
                                                                                         '1]/div[2]/div[2]/div['
                                                                                         '2]/div[2]/div[1]/div['
                                                                                         '1]/div[1]/app-login-normal['
                                                                                         '1]/div[1]/form[1]/div['
                                                                                         '5]/div[1]/a[1]')))

        self.driver.find_element(By.NAME, 'username').clear()
        self.driver.find_element(By.NAME, 'username').send_keys(self.userid)  # input username

        self.driver.find_element(By.XPATH, '/html[1]/body[1]/app-root[1]/app-right-root[1]/div[1]/div[2]/div[2]/div['
                                           '2]/div[2]/div[1]/div[1]/div[1]/app-login-normal[1]/div[1]/form[1]/div['
                                           '2]/nz-input-group[1]/input[1]').clear()
        self.driver.find_element(By.XPATH, '/html[1]/body[1]/app-root[1]/app-right-root[1]/div[1]/div[2]/div[2]/div['
                                           '2]/div[2]/div[1]/div[1]/div[1]/app-login-normal[1]/div[1]/form[1]/div['
                                           '2]/nz-input-group[1]/input[1]').send_keys(self.password)  # input password

        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入密码"]').send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userMessage')))
        self.driver.quit()

    def close(self):
        if self.driver is not None:
            self.driver.quit()


def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False


if __name__ == '__main__':
    '''
        ********注意********
    '''
    userid = '' # 填上自己的学号
    password = '' # 校园网密码
    address = 'https://id.dlmu.edu.cn/login?service=http:%2F%2F202.118.88.9%2Feportal%2Findex.jsp%3Fwlanuserip' \
              '%3De9f6276ead07a889b12918b791d1084d%26wlanacname%3Dc20f646d18ec8420743bb59779d3aa5d%26ssid%3D%26nasip' \
              '%3D321b8c06ed4b01461a74c22a11633718%26snmpagentip%3D%26mac%3D48d4e1ff97c68023dcc617f6664b53de%26t' \
              '%3Dwireless-v2%26url' \
              '%3D137959cd1821ef106bb9c54cf5e2fcecb2b61ecf1f18ce09a8820eaa59596fab9f8aef8adda54e5d%26apmac%3D%26nasid' \
              '%3Dc20f646d18ec8420743bb59779d3aa5d%26vid%3Dded60963ee687fd5%26port%3Da22a2c4b3e925766%26nasportid' \
              '%3Dc6abed3ee205e3f81369f2aee75d965812ee48161799ca327c02e2863c4c601e4f72911681b45e3d '
    log_file = 'log.log'
    # 配置日志文件
    log_cfg = LoggerConf(log_file)
    log_cfg.config()

    login = Login(userid=userid, password=password, addr=address)
    res = login.isNetOk()
    if res:
        logging.info("网络连接正常!")
    else:
        logging.info("网络未连接!")
        logging.info("尝试连接网络...")
        for i in range(1, 6):
            logging.info("第{}次尝试连接网络...".format(str(i)))
            try:
                login.auto_login()
            except Exception as e:
                logging.info("网络连接失败!")
                continue
            if login.isNetOk():
                logging.info("网络已成功连接！")
                break
            else:
                logging.info("网络连接失败!")

        if not login.isNetOk():
            login.close()
            logging.info("网络连接失败，等待人工检查...")
