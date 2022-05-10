import bz2
bz2_file = bz2.BZ2File(bz2_filename, 'w')
bz2_file.write(pdf_bytes)
bz2_file.close()
print("BZ2 파일 압축 완료")

#pdf 파일 생성
pdf_file = open(pdf_filename, 'wb')
pdf_file.write(pdf_bytes)
pdf_file.close()
print("PDF 파일 생성 완료")

#파일 압축 해제
bz2_file = bz2.BZ2File(bz2_filename, 'rb')
uncompressed_bytes = bz2_file.read()
bz2_file.close()
print("PDF 파일 압축 해제 완료")

#압축 해제한 
