package lab2.registration.model;

/**
 * Класс для базовой информации о курсе
 */
public class CourseInfo {

    /**
     * идентификатор курса
     */
    private long id;

    /**
     * название курса
     */
    private String name;

    /**
     * краткое описание курса
     */
    private String description;

    /**
     * Список идентификаторов курсов, которые нужно обязательно пройти до начала данного курса
     */
    private long[] prerequisites;

    /**
     * список категорий студентов, которые могут посещать курс
     */
    private StudentCategory[] studentCategories;

    // TODO: добавить геттеры и сеттеры {ГОТОВО}

    public long getId() {
        return this.id;
    }

    public long[] getPrerequisites() {
        return this.prerequisites;
    }

    public  StudentCategory[] getStudentCategories() {
        return this.studentCategories;
    }

}
