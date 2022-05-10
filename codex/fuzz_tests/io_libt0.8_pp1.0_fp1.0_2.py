import io.github.cepr0.demo.service.dto.PersonDto;
import io.github.cepr0.demo.service.dto.PersonRequest;
import org.springframework.stereotype.Component;

import java.util.function.Function;

@Component
public class PersonRequestMapper implements Function<PersonRequest, PersonDto> {

	@Override
	public PersonDto apply(final PersonRequest personRequest) {
		return PersonDto.builder()
				.name(personRequest.getName())
				.age(personRequest.getAge())
				.married(personRequest.isMarried())
				.build();
	}
}
