import selectInput from "../../../utils/selectInput";
import convertToDatetime from "../../../utils/convertToDatetime";
import { createBasicAlert } from "../../../utils/alerts";
import QUERIES from "../../../graphql/query";
import MUTATIONS from "../../../graphql/mutations";

const { useQuery, useMutation } = graphqlRequest(client);

const TodoForm = ({ todo, setShowForm, setShowAddBtn }) => {
  const [state, setState] = useState({
    title: todo?.title,
    description: todo?.description,
    date: todo?.date,
    time: todo?.time,
    is_done: todo?.is_done,
    todo_id: todo?.todo_id,
  });
  const handleChange = (e) => {
    const { name, value } = e.target;
    setState((prevState) => ({ ...prevState, [name]: value }));
  };

  const
