package img2pdf;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.itextpdf.text.DocumentException;
import com.itextpdf.text.Image;
import com.itextpdf.text.pdf.PdfWriter;

public class Main {
	public static void main(String[] args) throws DocumentException, IOException {

		String title = args[0];
		Path directory = Paths.get(title);
		int len = directory.toFile().listFiles().length;

		File pdf = new File(title + ".pdf");
		if (pdf.exists()) {
			System.out.println("PDF existed");
			return;
		}

		com.itextpdf.text.Document document = new com.itextpdf.text.Document();
		PdfWriter.getInstance(document, new FileOutputStream(pdf));
		
		document.open();
		for (int i = 0; i < len; i++) {
			File f = directory.resolve(String.format("%03d.jpg", i + 1)).toFile();
			Image img = Image.getInstance(f.getPath());
			document.setPageSize(img);
			document.newPage();
			img.setAbsolutePosition(0, 0);
			document.add(img);
		}
		document.close();
		System.out.println("PDF created");
		
	}
}
