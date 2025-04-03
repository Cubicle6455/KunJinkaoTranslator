def kunjinkao_detranslator(garbled_text):
    try:
        gbk_bytes = garbled_text.encode('gbk', errors='replace')
        original_text = gbk_bytes.decode('utf-8', errors='replace')

        return original_text
    except Exception as e:
        return f"还原失败: {str(e)}"

if __name__ == "__main__":
    input_text = input("请输入要还原的锟斤拷乱码文本: ")
    result = kunjinkao_detranslator(input_text)

    print("\n还原结果:")
    print(result)
