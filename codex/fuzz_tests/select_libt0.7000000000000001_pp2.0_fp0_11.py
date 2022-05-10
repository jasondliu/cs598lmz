import selectExclusiveCheckbox from '../../../methods/selectExclusiveCheckbox';
import { IProps as ICheckboxProps } from '../Checkbox';
import { IProps as ICheckboxGroupProps } from '../CheckboxGroup';
import { IProps as IRadioGroupProps } from '../RadioGroup';
import { IProps as IRadioProps } from '../Radio';
import { IProps as ISliderProps } from '../Slider';
import { IProps as ISwitchProps } from '../Switch';
import { IProps as ISelectProps } from '../Select';
import { IProps as ITextAreaProps } from '../TextArea';

export interface IFormItemProps extends IFormItem {
  children?: React.ReactNode;
  className?: string;
  style?: React.CSSProperties;
}

type IFormItemControl =
  | ICheckboxProps
  | ICheckboxGroupProps
  | IRadioGroupProps
  | IRadioProps
 
