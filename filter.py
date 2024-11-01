import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

class Person {
    private int id;
    private String name;

    // Constructor
    public Person(int id, String name) {
        this.id = id;
        this.name = name;
    }

    // Getters
    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return "Person{id=" + id + ", name='" + name + "'}";
    }
}

public class FilterExample {
    public static void main(String[] args) {
        // Sample list of persons
        List<Person> persons = new ArrayList<>();
        persons.add(new Person(1, "Alice"));
        persons.add(new Person(2, "Bob"));
        persons.add(new Person(3, "Charlie"));
        persons.add(new Person(4, "Alice"));

        // Filtering criteria
        String filterName = "Alice";
        int filterId = 1;

        // Filtering by name and id using Stream API
        List<Person> filteredList = persons.stream()
                .filter(p -> p.getName().equals(filterName) && p.getId() == filterId)
                .collect(Collectors.toList());

        // Output the filtered list
        System.out.println("Filtered Persons:");
        filteredList.forEach(System.out::println);
    }
}
