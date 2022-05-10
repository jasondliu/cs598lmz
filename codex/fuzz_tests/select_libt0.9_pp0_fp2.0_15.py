import selectClassData from '@/api/teacher-manage/select-class'

export default {
    data() {
        let me = this;
        let checkClassName = (rule, value, callback) => {
            if (!value) {
                return callback(new Error('教室名称不能为空'));
            }
            // if (value.length < 1) {
            //     callback(new Error('年龄至少为1位数字'));
            // }
            if (value.length > 30) {
                callback(new Error('年龄最多为30位字符'));
            }
            if(me.updateObj != null){
                if(me.updateObj.className == value){
                    callback();
                }
            }
            selectClassData.selectName(value).then(res =>{
                if(res.data.result){
                    callback();
                }else{
                    callback(new Error('教室
