import types
types.SimpleNamespace

def get_model(model_name, input_shape, num_classes, pretrained=None):
    if model_name == 'resnet18':
        model = resnet18(input_shape, num_classes, pretrained=pretrained)
    elif model_name == 'resnet34':
        model = resnet34(input_shape, num_classes, pretrained=pretrained)
    elif model_name == 'resnet50':
        model = resnet50(input_shape, num_classes, pretrained=pretrained)
    elif model_name == 'resnet101':
        model = resnet101(input_shape, num_classes, pretrained=pretrained)
    elif model_name == 'resnet152':
        model = resnet152(input_shape, num_classes, pretrained=pretrained)
    elif model_name == 'resnext50_32x4d':
        model = resnext50_32x4d(input_shape, num_classes, pretrained=pretrained)
