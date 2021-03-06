from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.views.generic import ListView


# Create your views here.
#class Homepage(ListView):
    #model = HomePage
    
def content (request):
    return render(request, 'landing/index.html',
    context={
        #Home Page
        'title_style_1': HomePage.objects.get(key='title_style_1').value,
        'title_style_2': HomePage.objects.get(key='title_style_2').value,
        'button_button_default': HomePage.objects.get(key='button_button_default').value,
        'subtitle_classic': HomePage.objects.get(key='subtitle_classic').value,
        'wow_fadeInLeft_1': HomePage.objects.get(key='wow_fadeInLeft_1').value,
        'wow_fadeInLeft_1_1': HomePage.objects.get(key='wow_fadeInLeft_1_1').value,
        'wow_fadeInLeft_1_2': HomePage.objects.get(key='wow_fadeInLeft_1_2').value,
        'wow_fadeInLeft_1_3': HomePage.objects.get(key='wow_fadeInLeft_1_3').value,
        'wow_fadeInRight_1': HomePage.objects.get(key='wow_fadeInRight_1').value,
        'wow_fadeInRight_2': HomePage.objects.get(key='wow_fadeInRight_2').value,
        'wow_fadeInRight_button': HomePage.objects.get(key='wow_fadeInRight_button').value,
        'subtitle_classic_2': HomePage.objects.get(key='subtitle_classic_2').value,
        'wow_fadeInLeft_2': HomePage.objects.get(key='wow_fadeInLeft_2').value,
        'wow_fadeInLeft_2_1': HomePage.objects.get(key='wow_fadeInLeft_2_1').value,
        'wow_fadeInLeft_2_2': HomePage.objects.get(key='wow_fadeInLeft_2_2').value,
        'wow_fadeInLeft_3': HomePage.objects.get(key='wow_fadeInLeft_3').value,
        'subtitle_classic_3': HomePage.objects.get(key='subtitle_classic_3').value,
        'd_inline_block': HomePage.objects.get(key='d_inline_block').value,
        'd_inline_block_2': HomePage.objects.get(key='d_inline_block_2').value,
        'project_classic_title': HomePage.objects.get(key='project_classic_title').value,
        'project_classic_tag': HomePage.objects.get(key='project_classic_tag').value,
        'project_classic_title_2': HomePage.objects.get(key='project_classic_title_2').value,
        'project_classic_tag_2': HomePage.objects.get(key='project_classic_tag_2').value,
        'project_classic_title_3': HomePage.objects.get(key='project_classic_title_3').value,
        'project_classic_tag_3': HomePage.objects.get(key='project_classic_tag_3').value,
        'project_classic_title_4': HomePage.objects.get(key='project_classic_title_4').value,
        'project_classic_tag_4': HomePage.objects.get(key='project_classic_tag_4').value,
        'project_classic_title_5': HomePage.objects.get(key='project_classic_title_5').value,
        'project_classic_tag_5': HomePage.objects.get(key='project_classic_tag_5').value,
        'project_classic_title_6': HomePage.objects.get(key='project_classic_title_6').value,
        'project_classic_tag_6': HomePage.objects.get(key='project_classic_tag_6').value,
        
        # Footer
        'base_preloader_title': HomePage.objects.get(key='base_preloader_title').value,
        'base_subtitle_classic': HomePage.objects.get(key='base_subtitle_classic').value,
        'base_d_inline_block': HomePage.objects.get(key='base_d_inline_block').value,
        'base_d_inline_block_2': HomePage.objects.get(key='base_d_inline_block_2').value,
        'base_contact_name': HomePage.objects.get(key='base_contact_name').value,
        'base_contact_email': HomePage.objects.get(key='base_contact_email').value,
        'base_contact_message': HomePage.objects.get(key='base_contact_message').value,
        'base_button_default': HomePage.objects.get(key='base_button_default').value,
        'base_rights_wow': HomePage.objects.get(key='base_rights_wow').value,
        'base_rights_wow_2': HomePage.objects.get(key='base_rights_wow_2').value,
        'base_rights_wow_3': HomePage.objects.get(key='base_rights_wow_3').value,
        'base_rights_wow_4': HomePage.objects.get(key='base_rights_wow_4').value,
        'base_rights_wow_5': HomePage.objects.get(key='base_rights_wow_5').value,

        # Menu
        'rd_nav_item_1': Menu.objects.get(key='rd_nav_item_1').value,
        'rd_nav_item_2': Menu.objects.get(key='rd_nav_item_2').value,
        'rd_nav_item_3': Menu.objects.get(key='rd_nav_item_3').value,
        'contacts_classic_title_1': Menu.objects.get(key='contacts_classic_title_1').value,
        'contacts_classic_title_1_1': Menu.objects.get(key='contacts_classic_title_1_1').value,
        'contacts_classic_title_2': Menu.objects.get(key='contacts_classic_title_2').value,
        'contacts_classic_title_2_1': Menu.objects.get(key='contacts_classic_title_2_1').value,
        'contacts_classic_title_3': Menu.objects.get(key='contacts_classic_title_3').value,
        #'fa_linkedin': Menu.objects.get(key='fa_linkedin').link,
        #'fa_twitter': Menu.objects.get(key='fa_twitter').link,
        #'fa_facebook': Menu.objects.get(key='fa_facebook').link,
        #'fa_instagram': Menu.objects.get(key='fa_instagram').link,


    })

    

    

def about (request):
    return render(request, 'landing/about.html', 
    context={

        # About Page
        'title': AboutUSModel.objects.get(key='title').value,
        'sec_2_subtitle': AboutUSModel.objects.get(key='sec_2_subtitle').value,
        'wow_fadeInLeft': AboutUSModel.objects.get(key='wow_fadeInLeft').value,
        'wow_fadeInLeft2': AboutUSModel.objects.get(key='wow_fadeInLeft2').value,
        'title_style_1': AboutUSModel.objects.get(key='title_style_1').value,
        'text_primary': AboutUSModel.objects.get(key='text_primary').value,
        'wow_fadeInRight_1': AboutUSModel.objects.get(key='wow_fadeInRight_1').value,
        'wow_fadeInRight_2': AboutUSModel.objects.get(key='wow_fadeInRight_2').value,
        'wow_fadeInUp': AboutUSModel.objects.get(key='wow_fadeInUp').value,
        'wow_fadeInLeft_1': AboutUSModel.objects.get(key='wow_fadeInLeft_1').value,
        'wow_fadeInRight_3': AboutUSModel.objects.get(key='wow_fadeInRight_3').value,
        'box_icon_modern_title': AboutUSModel.objects.get(key='box_icon_modern_title').value,
        'box_icon_modern_text': AboutUSModel.objects.get(key='box_icon_modern_text').value,
        'box_icon_modern_title_1': AboutUSModel.objects.get(key='box_icon_modern_title_1').value,
        'box_icon_modern_text_1': AboutUSModel.objects.get(key='box_icon_modern_text_1').value,
        'box_icon_modern_title_2': AboutUSModel.objects.get(key='box_icon_modern_title_2').value,
        'box_icon_modern_text_2': AboutUSModel.objects.get(key='box_icon_modern_text_2').value,
        'box_icon_modern_title_3': AboutUSModel.objects.get(key='box_icon_modern_title_3').value,
        'box_icon_modern_text_3': AboutUSModel.objects.get(key='box_icon_modern_text_3').value,
        'wow_fadeInUp_1': AboutUSModel.objects.get(key='wow_fadeInUp_1').value,
        'wow_fadeInLeft_4': AboutUSModel.objects.get(key='wow_fadeInLeft_4').value,
        'wow_fadeInRight_4': AboutUSModel.objects.get(key='wow_fadeInRight_4').value,
        'team_classic_name_1': AboutUSModel.objects.get(key='team_classic_name_1').value,
        'team_classic_status_1': AboutUSModel.objects.get(key='team_classic_status_1').value,
        'team_classic_name_2': AboutUSModel.objects.get(key='team_classic_name_2').value,
        'team_classic_status_2': AboutUSModel.objects.get(key='team_classic_status_2').value,
        'team_classic_name_3': AboutUSModel.objects.get(key='team_classic_name_3').value,
        'team_classic_status_3': AboutUSModel.objects.get(key='team_classic_status_3').value,
        
        #Footer
        'base_preloader_title': HomePage.objects.get(key='base_preloader_title').value,
        'base_subtitle_classic': HomePage.objects.get(key='base_subtitle_classic').value,
        'base_d_inline_block': HomePage.objects.get(key='base_d_inline_block').value,
        'base_d_inline_block_2': HomePage.objects.get(key='base_d_inline_block_2').value,
        'base_contact_name': HomePage.objects.get(key='base_contact_name').value,
        'base_contact_email': HomePage.objects.get(key='base_contact_email').value,
        'base_contact_message': HomePage.objects.get(key='base_contact_message').value,
        'base_button_default': HomePage.objects.get(key='base_button_default').value,
        'base_rights_wow': HomePage.objects.get(key='base_rights_wow').value,
        'base_rights_wow_2': HomePage.objects.get(key='base_rights_wow_2').value,
        'base_rights_wow_3': HomePage.objects.get(key='base_rights_wow_3').value,
        'base_rights_wow_4': HomePage.objects.get(key='base_rights_wow_4').value,
        'base_rights_wow_5': HomePage.objects.get(key='base_rights_wow_5').value,

        # Menu
        'rd_nav_item_1': Menu.objects.get(key='rd_nav_item_1').value,
        'rd_nav_item_2': Menu.objects.get(key='rd_nav_item_2').value,
        'rd_nav_item_3': Menu.objects.get(key='rd_nav_item_3').value,
        'contacts_classic_title_1': Menu.objects.get(key='contacts_classic_title_1').value,
        'contacts_classic_title_1_1': Menu.objects.get(key='contacts_classic_title_1_1').value,
        'contacts_classic_title_2': Menu.objects.get(key='contacts_classic_title_2').value,
        'contacts_classic_title_2_1': Menu.objects.get(key='contacts_classic_title_2_1').value,
        'contacts_classic_title_3': Menu.objects.get(key='contacts_classic_title_3').value,
        #'fa_linkedin': Menu.objects.get(key='fa_linkedin').link,
        #'fa_twitter': Menu.objects.get(key='fa_twitter').link,
        #'fa_facebook': Menu.objects.get(key='fa_facebook').link,
        #'fa_instagram': Menu.objects.get(key='fa_instagram').link,
    })

def contact (request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name,
            message,
            message_email,
            ['stetplace2020@gmail.com',message_email],
        )

        

        return render(request, 'landing/contacts.html', {'message_name': message_name},)

    else:
        return render(request, 'landing/contacts.html',
        context={
            # Contacts Page
            'title': ContactSModel.objects.get(key='title').value,
            'title_style_1': ContactSModel.objects.get(key='title_style_1').value,
            'contacts_modern_link': ContactSModel.objects.get(key='contacts_modern_link').value,
            'contacts_modern_link_2': ContactSModel.objects.get(key='contacts_modern_link_2').value,
            'contacts_modern_link_3_1': ContactSModel.objects.get(key='contacts_modern_link_3_1').value,
            'contacts_modern_link_3_2': ContactSModel.objects.get(key='contacts_modern_link_3_2').value,
            'contacts_modern_link_4': ContactSModel.objects.get(key='contacts_modern_link_4').value,
            'contacts_modern_link_5': ContactSModel.objects.get(key='contacts_modern_link_5').value,

            # Footer
            'base_preloader_title': HomePage.objects.get(key='base_preloader_title').value,
            'base_subtitle_classic': HomePage.objects.get(key='base_subtitle_classic').value,
            'base_d_inline_block': HomePage.objects.get(key='base_d_inline_block').value,
            'base_d_inline_block_2': HomePage.objects.get(key='base_d_inline_block_2').value,
            'base_contact_name': HomePage.objects.get(key='base_contact_name').value,
            'base_contact_email': HomePage.objects.get(key='base_contact_email').value,
            'base_contact_message': HomePage.objects.get(key='base_contact_message').value,
            'base_button_default': HomePage.objects.get(key='base_button_default').value,
            'base_rights_wow': HomePage.objects.get(key='base_rights_wow').value,
            'base_rights_wow_2': HomePage.objects.get(key='base_rights_wow_2').value,
            'base_rights_wow_3': HomePage.objects.get(key='base_rights_wow_3').value,
            'base_rights_wow_4': HomePage.objects.get(key='base_rights_wow_4').value,
            'base_rights_wow_5': HomePage.objects.get(key='base_rights_wow_5').value,

            # Menu
            'rd_nav_item_1': Menu.objects.get(key='rd_nav_item_1').value,
            'rd_nav_item_2': Menu.objects.get(key='rd_nav_item_2').value,
            'rd_nav_item_3': Menu.objects.get(key='rd_nav_item_3').value,
            'contacts_classic_title_1': Menu.objects.get(key='contacts_classic_title_1').value,
            'contacts_classic_title_1_1': Menu.objects.get(key='contacts_classic_title_1_1').value,
            'contacts_classic_title_2': Menu.objects.get(key='contacts_classic_title_2').value,
            'contacts_classic_title_2_1': Menu.objects.get(key='contacts_classic_title_2_1').value,
            'contacts_classic_title_3': Menu.objects.get(key='contacts_classic_title_3').value,
            #'fa_linkedin': Menu.objects.get(key='fa_linkedin').link,
            #'fa_twitter': Menu.objects.get(key='fa_twitter').link,
            #'fa_facebook': Menu.objects.get(key='fa_facebook').link,
            #'fa_instagram': Menu.objects.get(key='fa_instagram').link,
        })


