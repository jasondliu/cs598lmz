import io.micronaut.configuration.hibernate.ValidationHibernateConfigurations;
import io.micronaut.context.annotation.Bean;
import io.micronaut.context.annotation.Factory;
import io.micronaut.context.annotation.Parameter;
import io.micronaut.context.annotation.Prototype;
import io.micronaut.context.annotation.Requires;
import io.micronaut.context.exceptions.ConfigurationException;
import io.micronaut.core.reflect.ClassUtils;
import io.micronaut.core.reflect.InstantiationUtils;
import io.micronaut.core.util.CollectionUtils;
import io.micronaut.core.util.Toggleable;
import io.micronaut.inject.annotation.NamedAnnotationMapper;
import io.micronaut.inject.annotation.TypedAnnotationMapper;
import io.micronaut.validation.validator.constraints.ConstraintValidator;

import javax.inject
