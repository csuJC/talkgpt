import nls
import time

class AliyunTTS:
    def __init__(self, appkey, token):
        self.appkey = appkey
        self.token = token
        self.client = nls.NlsClient()
        self.client.set_log_level('INFO')

    def tts_callback(self, tts, message, *args):
        if message['header']['name'] == 'SynthesisCompleted':
            print('合成完成')
        elif message['header']['name'] == 'TaskFailed':
            print('合成失败:', message['header']['status_text'])

    def synthesize(self, text, output_file):
        tts = nls.NlsSpeechSynthesizer(
            url='wss://nls-gateway-cn-shanghai.aliyuncs.com/ws/v1',
            appkey=self.appkey,
            token=self.token,
            on_message=self.tts_callback
        )
        tts.start(text=text, voice='xiaoyun', format='wav', sample_rate=16000)
        with open(output_file, 'wb') as f:
            while True:
                data = tts.recv()
                if data is None:
                    break
                f.write(data)
        tts.stop()

if __name__ == '__main__':
    token="2d1ef4c006af432cb87645385bba4b30"   #参考https://help.aliyun.com/document_detail/450255.html获取token
    appkey="dl1Mp14q9s3RUEYe"      #获取Appkey请前往控制台：https://nls-portal.console.aliyun.com/applist

    tts = AliyunTTS(appkey, token)
    tts.synthesize('您好，这是一个测试。', 'output.wav')