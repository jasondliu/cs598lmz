import select from "../../../Tools/Selector/select";
import Auth from "../../../Tools/Auth";
const { ccclass, property } = cc._decorator;

@ccclass
export default class BoosMsg extends cc.Component {
    @property(cc.Node)
    Text = null;
    @property(cc.Node)
    img = null;
    @property(cc.Label)
    name = null;

    @property(cc.Label)
    fangzhi = null;
    @property(cc.Label)
    jifen = null;
    @property(cc.Label)
    youhui = null;

    @property(cc.Node)
    Roles = null;
    @property(cc.Node)
    Staff = null;
    @property(cc.Node)
    Title = null;
    @property(cc.Label)
    TextTrans = null;

    // LIFE-CYCLE CALLBACKS:

    // onLoad () {}

    @property(cc.Node)
    closeBtn = null;

    @
