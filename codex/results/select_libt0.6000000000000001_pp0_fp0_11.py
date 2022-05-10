import selected from '../../assets/icons/selected.svg';
import notSelected from '../../assets/icons/not-selected.svg';

export const ListItem = ({
  item,
  index,
  handleSelect,
  selectedItemIndex,
  handleDeleteItem,
}) => {
  const [isSelected, setIsSelected] = useState(false);
  const [isHovered, setIsHovered] = useState(false);

  const handleMouseEnter = () => {
    setIsHovered(true);
  };

  const handleMouseLeave = () => {
    setIsHovered(false);
  };

  const handleSelectItem = () => {
    handleSelect(item);
    setIsSelected(true);
  };

  useEffect(() => {
    if (index === selectedItemIndex) {
      setIsSelected(true);
    } else {
      setIsSelected(false);
    }
  }, [selectedItemIndex]);

  return (
    <Container
      isSelected={isSelected}
      on
