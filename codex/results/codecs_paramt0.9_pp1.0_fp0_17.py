import codecs
codecs.register_error('strict', codecs.ignore_errors)
open('zh_CN.sdf', 'w', encoding='utf_8_sig').write(open('zh_CN.sdf', encoding='utf_8').read())

# # 提取所有模块
# import re
#
# s = open('openerp_all.txt', 'w')
# def write_name(m):
#     if re.match(r'^#', m):
#         return False
#     s.write(re.split(r'\s+', m)[1].strip() + '\n')
#     return True
#
# for m in open('addons_all.txt'):
#     write_name(m)
# for m in open('addons_deprecated.txt'):
#     write_name(m)
# for m in open('server_modules.txt'):
#     s.write(re.split(r'\s+', m)[0].strip() + '\n')

# 输出

