#!/usr/bin/env python3
import fal_client
import os
import requests
from urllib.parse import urlparse

# Set up FAL API
os.environ["FAL_KEY"] = "ce22005f-5a8d-439c-a504-18f75b1884af:f719a67db4b43c8acfa24d298f097a7f"

# Brand colors for reference in prompts
brand_colors = {
    'charcoal': '#1A1A2E',
    'orange': '#E8720C', 
    'red': '#C62828',
    'gray': '#B0BEC5',
    'gold': '#D4A017',
    'white': '#F5F5F5'
}

# Image prompts for the 9-post grid
prompts = [
    # 1. Hero brand shot
    """Professional commercial photography of a black dumpster on a clean residential driveway during golden hour, with Kansas City skyline subtly visible in the background. Clean modern industrial aesthetic, premium lighting, space for text overlay, charcoal and orange color scheme, high-end construction brand feel, 1080x1080 aspect ratio""",
    
    # 2. Before/After split
    """Split-screen before and after image: LEFT side shows a cluttered messy garage full of junk and debris, RIGHT side shows the same garage completely clean and organized. Clean split down the middle, industrial modern style, dramatic transformation, dumpster rental concept, premium aesthetic, 1080x1080""",
    
    # 3. Pricing graphic
    """Clean modern pricing graphic design with dark charcoal background (#1A1A2E), bright industrial orange accents (#E8720C). Text showing "15 YARD $300/week" and "20 YARD $400/week". Minimalist industrial design, premium construction brand aesthetic, bold typography, 1080x1080 square format""",
    
    # 4. Happy customer testimonial
    """Professional photo of a satisfied middle-aged homeowner giving thumbs up next to a black dumpster at a residential home renovation project. Natural lighting, genuine smile, construction work in background, premium dumpster rental service, realistic commercial photography style, 1080x1080""",
    
    # 5. Brand logo/mission
    """Dark industrial brand design with charcoal background (#1A1A2E) and bright orange accents (#E8720C). Text reading "FSR DUMPSTERS" and "Premium Waste Solutions for Kansas City". Bold modern typography, industrial construction aesthetic, premium brand identity, 1080x1080""",
    
    # 6. Dumpster delivery action
    """Action shot of a professional truck delivering a black dumpster to a suburban house. Motion blur suggesting movement, truck backing into driveway, residential neighborhood setting, professional service delivery, industrial premium aesthetic, dynamic composition, 1080x1080""",
    
    # 7. Educational tips
    """Modern infographic design with dark charcoal background showing "5 THINGS TO KNOW BEFORE RENTING A DUMPSTER". Clean numbered list layout, industrial orange accents (#E8720C), premium educational content design, bold readable typography, professional construction industry feel, 1080x1080""",
    
    # 8. KC local pride
    """Kansas City skyline silhouette with iconic landmarks, featuring a dumpster rental truck in the foreground. Golden hour lighting, local pride theme, premium industrial aesthetic, subtle "SERVING KANSAS CITY METRO" text, charcoal and orange color scheme, professional photography style, 1080x1080""",
    
    # 9. CTA booking post
    """Bold call-to-action design with dark background and bright orange elements. Large text "BOOK YOUR DUMPSTER TODAY" with phone number placeholder area. Modern industrial aesthetic, premium construction brand feel, compelling CTA design, high contrast typography, 1080x1080"""
]

# File names for each image
filenames = [
    "01_hero_brand.jpg",
    "02_before_after.jpg", 
    "03_pricing_graphic.jpg",
    "04_customer_testimonial.jpg",
    "05_brand_mission.jpg",
    "06_delivery_action.jpg",
    "07_educational_tips.jpg",
    "08_kc_local_pride.jpg",
    "09_cta_booking.jpg"
]

def download_image(url, filepath):
    """Download image from URL to local filepath"""
    response = requests.get(url)
    response.raise_for_status()
    with open(filepath, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded: {filepath}")

def generate_image(prompt, filename):
    """Generate a single image using fal.ai"""
    print(f"Generating {filename}...")
    try:
        handler = fal_client.submit(
            "fal-ai/flux-pro/v1.1-ultra", 
            arguments={
                "prompt": prompt,
                "num_images": 1,
                "aspect_ratio": "1:1",
                "safety_tolerance": "5",
                "raw": True
            }
        )
        result = handler.get()
        
        # Download the image
        image_url = result["images"][0]["url"]
        filepath = f"/Users/centralhq/.openclaw/workspace/projects/fsr-dumpsters/instagram/{filename}"
        download_image(image_url, filepath)
        
        return True
    except Exception as e:
        print(f"Error generating {filename}: {str(e)}")
        return False

def main():
    print("Generating FSR Dumpsters Instagram grid images...")
    print(f"Total images to generate: {len(prompts)}")
    
    successful = 0
    for i, (prompt, filename) in enumerate(zip(prompts, filenames)):
        print(f"\nImage {i+1}/9:")
        if generate_image(prompt, filename):
            successful += 1
        
    print(f"\nGeneration complete: {successful}/{len(prompts)} images successful")

if __name__ == "__main__":
    main()