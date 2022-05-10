import selected from "./selected";
import props from "./props";
import defaultWidth from "./defaultWidth";
import propsData from "./propsData";
import renderers from "./renderers";

export default function (node, index, store) {
    var propsMetadata = utils.num2str(node.propsMetadata);
    var object = store.objects[propsMetadata];
    if (object) {
        selected(node, index, store);
        var propsStr = utils.num2str(object.props);
        var propsObj = store.objects[propsStr];
        if (propsObj) {
            props(node, index, store, propsObj);
        }
        var widthStr = utils.num2str(object.width);
        var widthObj = store.objects[widthStr];
        if (widthObj) {
            defaultWidth(node, index, store, widthObj);
        }
        var propsDataStr = utils.num2str(object.propsData);
        if (propsDataStr) {
            var
