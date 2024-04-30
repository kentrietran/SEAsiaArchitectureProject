$(document).ready(function() {
    var currentIndex = 0;
    var totalImages = $('.gallery img').length;

    updateGallery();

    // Hide all images and captions except the one corresponding to the current index
    $('.gallery img').hide().eq(currentIndex).show();
    $('.lesson-card-caption').hide().eq(currentIndex).show();

    $('.prev').click(function() {
        if (currentIndex > 0) {
            currentIndex--;
            updateGallery();
        }
    });

    $('.next').click(function() {
        if (currentIndex < totalImages - 1) {
            currentIndex++;
            updateGallery();
        }
    });

    // Function to update gallery
    function updateGallery() {
        // Hide all images and captions except the one corresponding to the current index
        if (currentIndex === 0) {
            $('.prev').css('background-color', '#8b8c89'); // Change background color to gray
            $('.prev').css('border', '1px solid #8b8c89');
        } else{
            $('.prev').css('background-color', '#a2d2ffff');
            $('.prev').css('border', '1px solid #a2d2ffff');
            // Add hover effect to buttons
            $('.prev').hover(function() {
                if (currentIndex === 0) {
                    $('.prev').css('background-color', '#8b8c89');
                } else{
                    $('.prev').css('background-color', 'rgb(124, 192, 255)');
                }
            }, function() {
                if (currentIndex === 0) {
                    $('.prev').css('background-color', '#8b8c89');
                } else{
                    $('.prev').css('background-color', '#a2d2ffff');
                }
            });
        }
    
        if(currentIndex === totalImages - 1){
            $('.next').css('background-color', '#8b8c89'); // Change background color to gray
            $('.next').css('border', '1px solid #8b8c89');
        } else{
            $('.next').css('background-color', '#a2d2ffff');
            $('.next').css('border', '1px solid #a2d2ffff');
            // Add hover effect to buttons
            $('.next').hover(function() {
                if (currentIndex === totalImages - 1) {
                    $('.next').css('background-color', '#8b8c89');
                } else{
                    $('.next').css('background-color', 'rgb(124, 192, 255)');
                }
            }, function() {
                if (currentIndex === totalImages - 1) {
                    $('.next').css('background-color', '#8b8c89');
                } else{
                    $('.next').css('background-color', '#a2d2ffff');
                }
            });
        }
        $('.gallery img').hide().eq(currentIndex).show();
        $('.lesson-card-caption').hide().eq(currentIndex).show();
    }
});
