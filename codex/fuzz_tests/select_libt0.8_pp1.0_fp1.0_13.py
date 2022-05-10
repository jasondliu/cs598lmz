import selectVip from "../../../components/selectsearch/selectsearch";
import search from "../../../components/search/search";
import {
  memberCardList,
  membersList,
  vipLevelList,
  vipLevelFind,
  vipLevelUpdate,
  vipLevelDelete
} from "../../../api/member/vipManage";
import { Loading, Message } from 'element-ui';
import {selectType,selectSearchType} from "../../../components/selectsearch/selectType"
import { setCookie, getCookie } from "../../../utils/common";
let vm = null,
  globalData = getApp().globalData;
Page({
  data: {
    page: 1,
    size: 10,
    total: 0,
    shopId: '',
    shopList: [],
    title: '会员管理',
    list: [],
    type: 1,
    dialogShow: false,
    buttons: [],
    type_text: "",
    classifys
