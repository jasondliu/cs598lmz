from _struct import Struct
s = Struct.__new__(Struct)
s.format = '10s5s5s5s5s5s5s5s5s5s5s'

print(s.parse(_struct_i.pack(100,100,100,100,100,100,100,100,100,100)))


class type2_22(type2):
    def __init__(self, length=default_length, syncword=default_syncword,
                 crc_scheme=default_crc_scheme, duplex_spacing=default_duplex_spacing,
                 data_transfer_device=default_data_transfer_device, ui_frame=default_ui_frame):
        super(type2_22, self).__init__(length=length, syncword=syncword,
              crc_scheme=crc_scheme, duplex_spacing=duplex_spacing,
              data_transfer_device=data_transfer_device, ui_frame=ui_frame)
        self.s = Struct(':I')

    def serialize(self):
        binval = super(type
