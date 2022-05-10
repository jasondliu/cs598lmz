import _struct from '../base/_struct';

export default class C_LA_A_7_T extends _struct {
    constructor() {
        super();

        this.name = '设备类型';
        this.desc = '有关设备类型的各种信息';

        this.originator = 0x30;
        this.control = 0x1F;
        this.control_func = 0xFF;

        this.sub_control = 0x02;
        this.sub_control_func = 0xFF;

        this.main_data = [];

        this.sub_data = [];

        this.sub_data_list = {
            0x01: ['设备类型', 'B'],
            0x02: ['协议版本', 'B'],
            0x03: ['设备序列号', 'H5'],
            0x04: ['设
