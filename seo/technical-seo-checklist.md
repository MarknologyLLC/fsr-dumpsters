# FSR Dumpsters - Technical SEO Checklist

## robots.txt Configuration

### Recommended robots.txt Content
```
User-agent: *
Allow: /

# Specific paths to allow (if needed)
Allow: /images/
Allow: /css/
Allow: /js/

# Disallow admin/sensitive areas (if applicable)
# Disallow: /admin/
# Disallow: /private/

# Sitemap location
Sitemap: https://fsrdumpsters.com/sitemap.xml

# Additional sitemaps (if using multiple)
# Sitemap: https://fsrdumpsters.com/sitemap-images.xml
# Sitemap: https://fsrdumpsters.com/sitemap-local.xml
```

### robots.txt Best Practices
- ✅ Place robots.txt at domain root (https://fsrdumpsters.com/robots.txt)
- ✅ Keep it simple for a single-page site
- ✅ Include sitemap URL
- ✅ Test with Google Search Console robots.txt tester
- ✅ Update if adding restricted areas later

## sitemap.xml Structure

### Basic XML Sitemap
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  
  <!-- Homepage -->
  <url>
    <loc>https://fsrdumpsters.com/</loc>
    <lastmod>2024-02-28</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  
  <!-- Services Section -->
  <url>
    <loc>https://fsrdumpsters.com/#services</loc>
    <lastmod>2024-02-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  
  <!-- Service Areas Section -->
  <url>
    <loc>https://fsrdumpsters.com/#service-areas</loc>
    <lastmod>2024-02-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  
  <!-- FAQ Section -->
  <url>
    <loc>https://fsrdumpsters.com/#faq</loc>
    <lastmod>2024-02-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  
  <!-- Contact Section -->
  <url>
    <loc>https://fsrdumpsters.com/#contact</loc>
    <lastmod>2024-02-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  
</urlset>
```

### Sitemap Submission Checklist
- ✅ Upload sitemap.xml to domain root
- ✅ Submit to Google Search Console
- ✅ Submit to Bing Webmaster Tools
- ✅ Include sitemap URL in robots.txt
- ✅ Update lastmod dates when content changes
- ✅ Validate XML syntax before uploading

## Canonical URLs

### Canonical Tag Implementation
```html
<!-- Primary homepage canonical -->
<link rel="canonical" href="https://fsrdumpsters.com/" />
```

### Canonical URL Best Practices
- ✅ Use absolute URLs (https://fsrdumpsters.com/)
- ✅ Self-referencing canonical on main page
- ✅ Ensure consistency across all pages
- ✅ Include canonical in HTML `<head>` section
- ✅ Use lowercase URLs for consistency
- ✅ Include trailing slash consistently

### URL Structure Guidelines
- **Preferred format:** https://fsrdumpsters.com/ (with trailing slash)
- **Avoid:** https://www.fsrdumpsters.com (if not using www)
- **Avoid:** http:// (always use HTTPS)
- **Avoid:** Mixed case URLs

## Open Graph Tags

### Essential Open Graph Meta Tags
```html
<!-- Basic Open Graph Tags -->
<meta property="og:title" content="Dumpster Rental Kansas City - FSR Dumpsters | 15 & 20 Yard Roll Off" />
<meta property="og:description" content="Kansas City dumpster rental service. 15 & 20 yard roll off dumpsters starting at $300/week. Same day delivery. Serving 7 counties in MO & KS. Call (816) 555-1234." />
<meta property="og:type" content="business.business" />
<meta property="og:url" content="https://fsrdumpsters.com/" />
<meta property="og:site_name" content="FSR Dumpsters" />

<!-- Open Graph Images -->
<meta property="og:image" content="https://fsrdumpsters.com/images/fsr-dumpsters-og-image.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="FSR Dumpsters - Kansas City roll off dumpster rental service" />

<!-- Business-Specific Open Graph -->
<meta property="business:contact_data:street_address" content="6308 N Main St" />
<meta property="business:contact_data:locality" content="Gladstone" />
<meta property="business:contact_data:region" content="MO" />
<meta property="business:contact_data:postal_code" content="64118" />
<meta property="business:contact_data:country_name" content="USA" />
<meta property="business:contact_data:phone_number" content="8165551234" />
<meta property="business:contact_data:website" content="https://fsrdumpsters.com" />

<!-- Facebook App ID (if applicable) -->
<!-- <meta property="fb:app_id" content="YOUR_FACEBOOK_APP_ID" /> -->
```

### Open Graph Image Requirements
- **Dimensions:** 1200x630 pixels (recommended)
- **File format:** JPG or PNG
- **File size:** Under 8MB
- **Content:** FSR Dumpsters logo, dumpster image, contact info
- **File name:** fsr-dumpsters-og-image.jpg

## Twitter Card Tags

### Twitter Card Meta Tags
```html
<!-- Twitter Card Tags -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Dumpster Rental Kansas City - FSR Dumpsters | Same Day Service" />
<meta name="twitter:description" content="Kansas City dumpster rental. 15 & 20 yard containers starting at $300/week. Same day delivery available. Serving 7 counties. Call (816) 555-1234." />
<meta name="twitter:image" content="https://fsrdumpsters.com/images/fsr-dumpsters-twitter-card.jpg" />
<meta name="twitter:image:alt" content="FSR Dumpsters Kansas City dumpster rental service" />

<!-- Twitter Business Info -->
<meta name="twitter:site" content="@fsrdumpsters" />
<meta name="twitter:creator" content="@fsrdumpsters" />
```

### Twitter Card Image Requirements
- **Dimensions:** 1200x675 pixels (16:9 ratio)
- **File format:** JPG, PNG, WEBP, or GIF
- **File size:** Under 5MB
- **Content:** Professional dumpster image with FSR branding

## Mobile Optimization Requirements

### Viewport Meta Tag
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
```

### Mobile-Friendly Checklist
- ✅ Responsive design that adapts to all screen sizes
- ✅ Touch-friendly buttons (minimum 44px tap targets)
- ✅ Readable font sizes (minimum 16px on mobile)
- ✅ Fast loading times on mobile networks
- ✅ Easy-to-use contact forms on mobile
- ✅ Click-to-call phone numbers
- ✅ Optimized images for mobile bandwidth
- ✅ No horizontal scrolling required
- ✅ Mobile-friendly navigation menu

### CSS Media Query Strategy
```css
/* Mobile First Approach */
/* Base styles for mobile (320px and up) */

@media (min-width: 768px) {
  /* Tablet styles */
}

@media (min-width: 1024px) {
  /* Desktop styles */
}

@media (min-width: 1200px) {
  /* Large desktop styles */
}
```

## Page Speed Recommendations

### Core Web Vitals Targets
- **Largest Contentful Paint (LCP):** < 2.5 seconds
- **First Input Delay (FID):** < 100 milliseconds  
- **Cumulative Layout Shift (CLS):** < 0.1

### Speed Optimization Checklist
- ✅ Optimize and compress all images
- ✅ Enable GZIP compression
- ✅ Minimize HTTP requests
- ✅ Use a Content Delivery Network (CDN)
- ✅ Minimize CSS and JavaScript files
- ✅ Enable browser caching
- ✅ Optimize web fonts loading
- ✅ Remove unused CSS and JavaScript
- ✅ Implement lazy loading for images
- ✅ Use modern image formats (WebP)

### Image Optimization Guidelines
- **Format:** Use WebP with JPG fallback
- **Compression:** 80-85% quality for photos
- **Dimensions:** Serve images at exact display size
- **Loading:** Implement lazy loading for below-fold images
- **Alt text:** Required for all images (see below)

### Critical CSS Implementation
```html
<style>
/* Inline critical CSS for above-the-fold content */
/* This includes header, hero section, and initial content styling */
</style>

<!-- Load non-critical CSS asynchronously -->
<link rel="preload" href="/css/main.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
```

## Alt Text for Images

### Alt Text Strategy and Examples

#### Logo Images
```html
<img src="fsr-dumpsters-logo.png" alt="FSR Dumpsters Kansas City dumpster rental service logo" />
```

#### Product Images
```html
<!-- 15-yard dumpster -->
<img src="15-yard-dumpster.jpg" alt="15-yard roll off dumpster for residential cleanouts in Kansas City" />

<!-- 20-yard dumpster -->
<img src="20-yard-dumpster.jpg" alt="20-yard roll off dumpster for construction debris removal Kansas City" />

<!-- Delivery truck -->
<img src="delivery-truck.jpg" alt="FSR Dumpsters delivery truck placing roll off container at Kansas City home" />
```

#### Service Area Images
```html
<img src="kansas-city-skyline.jpg" alt="Kansas City Missouri skyline showing FSR Dumpsters service area" />
<img src="gladstone-location.jpg" alt="FSR Dumpsters location at 6308 N Main St Gladstone Missouri" />
```

#### Process/How-It-Works Images
```html
<img src="dumpster-delivery-process.jpg" alt="Professional dumpster delivery process by FSR Dumpsters Kansas City" />
<img src="same-day-delivery.jpg" alt="Same day dumpster delivery service available in Kansas City Metro" />
```

### Alt Text Best Practices
- ✅ Include target keywords naturally
- ✅ Describe the image content accurately
- ✅ Keep under 125 characters when possible
- ✅ Include location keywords for local SEO
- ✅ Don't start with "Image of" or "Picture of"
- ✅ Be specific about dumpster sizes and services
- ✅ Include context about the service or location

## Technical Implementation Checklist

### HTML Head Section Template
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- SEO Meta Tags -->
  <title>Dumpster Rental Kansas City - FSR Dumpsters | 15 & 20 Yard Roll Off | Same Day Service</title>
  <meta name="description" content="Kansas City dumpster rental service. 15 & 20 yard roll off dumpsters starting at $300/week. Serving Clay, Jackson, Platte, Cass, Johnson, Wyandotte & Leavenworth counties. Same day delivery available. Call (816) 555-1234.">
  
  <!-- Canonical URL -->
  <link rel="canonical" href="https://fsrdumpsters.com/" />
  
  <!-- Open Graph Tags -->
  [Open Graph tags from above]
  
  <!-- Twitter Card Tags -->
  [Twitter Card tags from above]
  
  <!-- Critical CSS -->
  <style>[Critical CSS]</style>
  
  <!-- Schema Markup -->
  <script type="application/ld+json">
    [JSON-LD schema from schema-markup.json]
  </script>
  
  <!-- Favicon -->
  <link rel="icon" type="image/x-icon" href="/favicon.ico">
  
</head>
```

### Testing and Validation Tools
- **Google PageSpeed Insights:** Test mobile and desktop performance
- **Google Search Console:** Monitor search performance and issues
- **Google Rich Results Test:** Validate schema markup
- **Facebook Sharing Debugger:** Test Open Graph implementation
- **Twitter Card Validator:** Test Twitter Card implementation
- **W3C Markup Validator:** Validate HTML structure
- **Google Mobile-Friendly Test:** Ensure mobile compatibility

### Monthly Technical SEO Tasks
- ✅ Check Google Search Console for errors
- ✅ Run PageSpeed Insights tests
- ✅ Validate schema markup
- ✅ Test all contact forms and CTAs
- ✅ Verify sitemap is up to date
- ✅ Monitor Core Web Vitals
- ✅ Check for broken links
- ✅ Review mobile usability reports
- ✅ Update lastmod dates in sitemap when content changes
- ✅ Monitor keyword rankings and adjust as needed