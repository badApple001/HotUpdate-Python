#!/usr/bin/env python
import base64
from Crypto.Cipher import AES

'''
采用AES对称加密算法
'''
key = 'abc5576890acb456' #加密KEY

# str不是16的倍数那就补足为16的倍数
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes

# 加密方法
def encrypt( mystr:str ):
    text = base64.b64encode(mystr.encode('utf-8')).decode('ascii')
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    # 先进行AES加密
    encrypt_AES = aes.encrypt(add_to_16(text))
    # 用base64转成字符串形式
    encrypted_text = str(base64.encodebytes(encrypt_AES), encoding='utf-8')  # 执行加密并转码返回bytes
    return encrypted_text

# 解密方法
def decrypt( text:str ):
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    # 优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
    # bytes解密
    decrypted_text = str(aes.decrypt(base64_decrypted),encoding='utf-8') # 执行解密密并转码返回str
    decrypted_text = base64.b64decode(decrypted_text.encode('utf-8')).decode('utf-8')
    return decrypted_text