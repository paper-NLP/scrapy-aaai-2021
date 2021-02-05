import glob
import fitz  # 导入本模块需安装pymupdf库
import os

# 将文件夹中所有jpg图片全部转换为一个指定名称的pdf文件，并保存至指定文件夹
def pic2pdf_1(img_path, pdf_path, pdf_name):
    doc = fitz.open()

    for img in sorted(glob.glob(img_path + "/*.jpg")):
        imgdoc = fitz.open(img)
        pdfbytes = imgdoc.convertToPDF()
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)
    doc.save(pdf_path + pdf_name)
    doc.close()

if __name__ == '__main__':
    img_path = r'/Users/i/Code/scrapy/aaai/images'
    pdf_path = r'/Users/i/Code/scrapy/aaai/pdf/'

    for file in os.scandir(img_path):
        if file.is_dir():
            pic2pdf_1(img_path=file.path, pdf_path=pdf_path, pdf_name='{}.pdf'.format(file.name))
