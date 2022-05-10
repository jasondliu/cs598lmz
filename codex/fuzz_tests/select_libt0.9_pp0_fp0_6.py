import selector from '../../../../theme/selectors';

const StyledTitle = styled.h1`
  font-size: 24px;
  line-height: 24px;
  color: ${selector('whiteColor')};
  text-decoration: none;
  transition: all 300ms ease;
`;

StyledTitle.defaultProps = {
  theme: ThemeDefault,
};

export default StyledTitle;
