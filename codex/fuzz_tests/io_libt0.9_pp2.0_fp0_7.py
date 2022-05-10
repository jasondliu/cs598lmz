import io.jsd.training.topic.Topic;

@Service 
public class CourseService {

	@Autowired	
	private CourseRepository courseRepository;
	
	public List<Course> getAllCourses(String id){
		List<Course> courses = new ArrayList<>();
		courseRepository.findByTopicId(id).forEach(courses::add);
		return courses;
	}
	
	public Course getCorse(String id){
		return courseRepository.findOne(id);
	}
	
	public void addCourse (Course course){
		courseRepository.save(course);
	}
	
	public void updateCourse (Course course){
		courseRepository.save(course);
	}
	
	public void deleteCourse (String id){
		courseRepository.deleteById(id);
	}
}
