import java.util.ArrayList;
import java.util.List;
public class LibraryManager {
private List<Book> books = new ArrayList<>();
public void addBook(Book book) {
books.add(book);
System.out.println("Da them sach thanh
cong!");
}
public void displayBooks() {
for (Book b : books) {
System.out.println(b);
}
}
}