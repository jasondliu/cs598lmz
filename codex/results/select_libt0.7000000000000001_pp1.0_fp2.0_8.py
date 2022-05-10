import selector from "./selector";

interface IProps {
    match: { params: { id: string } };
}

const Character = (props: IProps) => {
    const {
        match: {
            params: { id },
        },
    } = props;
    const { data: character, loading, error } = useSelector(
        (state: any) => selector(state, id),
    );

    return (
        <div>
            <h2>Character</h2>
            {loading && <p>Loading...</p>}
            {error && <p>Error: {error}</p>}
            {character && (
                <>
                    <p>Name: {character.name}</p>
                    <p>
                        Species:{" "}
                        <ul>
                            {character.species.map((s: string) => (
                                <li>{s}</li>
                            ))}
                        </ul>
                    </p>
                    <p>
                        Residents:{" "}
                        <ul>
