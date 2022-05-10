import selectors from "../../selectors";

describe("ExpensesListItem", () => {
  test("should render ExpensesListItem with expense", () => {
    const expense = {
      ...expenses[0],
      description: undefined
    };
    const wrapper = shallow(<ExpensesListItem {...expense} />);
    expect(wrapper).toMatchSnapshot();
  });

  test("should render ExpensesListItem with id", () => {
    const expense = {
      ...expenses[0],
      id: "12345",
      description: undefined
    };
    const wrapper = shallow(<ExpensesListItem {...expense} />);
    expect(wrapper).toMatchSnapshot();
  });
});
