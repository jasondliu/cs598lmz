import io.leangen.graphql.annotations.GraphQLArgument;
import io.leangen.graphql.annotations.GraphQLQuery;

@Component
public class EventResolver {

    @Autowired
    private EventRepository eventRepository;

    @GraphQLQuery(name = "events")
    public List<Event> getEvents() {
        return eventRepository.findAll();
    }

    @GraphQLQuery(name = "event")
    public Optional<Event> getEventById(@GraphQLArgument(name = "id") String id) {
        return eventRepository.findById(id);
    }
}
