def kunjinkao_translator(text):
    try:
        # 将UTF-8文本编码为字节串
        utf8_bytes = text.encode('utf-8')

        # 错误地将UTF-8字节串用GBK解码
        gbk_decoded = utf8_bytes.decode('gbk', errors='replace')

        return gbk_decoded
    except Exception as e:
        return f"转换失败: {str(e)}"

if __name__ == "__main__":
    input_text = input("请输入要转换为锟斤拷语的UTF-8文本: ")
    result = kunjinkao_translator(input_text)
    print("\n锟斤拷语转换结果:")
    print(result)
